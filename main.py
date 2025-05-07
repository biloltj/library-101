import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QInputDialog
from app.library_ui import Ui_MainWindow
from app.library import load_library, save_library
from datetime import datetime, timedelta

class LibraryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_data()

        self.ui.btnSearch.clicked.connect(self.search_book)
        self.ui.btnBorrow.clicked.connect(self.borrow_book)
        self.ui.btnReturn.clicked.connect(self.return_book)
        self.ui.btnHistory.clicked.connect(self.view_history)
        self.ui.btnListBooks.clicked.connect(self.list_books)
        self.ui.btnExit.clicked.connect(self.close)

    def load_data(self):
        """Reload library data from file."""
        self.library = load_library()

    def search_book(self):
        self.load_data()  
        title_input = self.ui.inputTitle.text().strip().lower()
        self.ui.textOutput.clear()

        for title, book in self.library.items():
            if title.lower() == title_input:
                status = "✅ Available" if book["available"] else f"❌ Borrowed by {book['borrower']}"
                self.ui.textOutput.append(f"'{title}' by {book['author']} — {status}")
                return

        self.ui.textOutput.append("🚫 Book not found.")

    def borrow_book(self):
        self.load_data()
        title_input = self.ui.inputTitle.text().strip().lower()
        self.ui.textOutput.clear()

        
        for title, book in self.library.items():
            if title.lower() == title_input:
                if not book["available"]:
                    self.ui.textOutput.append(f"❌ Already borrowed by {book['borrower']}")
                    return

                borrower, ok = QInputDialog.getText(self.ui.centralwidget, "Borrow Book", "Enter borrower's name:")
                if not ok or not borrower.strip():
                    self.ui.textOutput.append("⚠️ Borrow cancelled.")
                    return

                borrower = borrower.strip().title()
                due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")

                book.update({
                    "available": False,
                    "borrower": borrower,
                    "due_date": due_date
                })
                book["history"].append([borrower, datetime.now().strftime("%Y-%m-%d"), None])
                save_library(self.library)
                self.ui.textOutput.append(f"✅ '{title}' borrowed by {borrower} until {due_date}.")
                return

        self.ui.textOutput.append("🚫 Book not found.")

    def return_book(self):
        self.load_data()
        title_input = self.ui.inputTitle.text().strip().lower()
        self.ui.textOutput.clear()

        for title, book in self.library.items():
            if title.lower() == title_input:
                if book["available"]:
                    self.ui.textOutput.append("ℹ️ Book is already available.")
                    return

                returner, ok = QInputDialog.getText(self.ui.centralwidget, "Return Book", "Enter returner's name:")
                if not ok or not returner.strip():
                    self.ui.textOutput.append("⚠️ Return cancelled.")
                    return

                returner = returner.strip().title()
                return_date = datetime.now().strftime("%Y-%m-%d")
                previous_borrower = book["borrower"]

                book.update({
                    "available": True,
                    "borrower": None,
                    "due_date": None
                })

                if book["history"] and book["history"][-1][2] is None:
                    last = book["history"][-1]
                    book["history"][-1] = [last[0], last[1], return_date]

                save_library(self.library)
                self.ui.textOutput.append(f"✅ '{title}' returned by {returner}. Previously borrowed by {previous_borrower}.")
                return

        self.ui.textOutput.append("🚫 Book not found.")

    def view_history(self):
        self.load_data()
        title_input = self.ui.inputTitle.text().strip().lower()
        self.ui.textOutput.clear()

        for title, book in self.library.items():
            if title.lower() == title_input:
                self.ui.textOutput.append(f"🕓 History for '{title}':")
                for borrower, date_borrowed, date_returned in book["history"]:
                    returned = date_returned or "⏳ Not yet returned"
                    self.ui.textOutput.append(f"{borrower} — Borrowed on {date_borrowed}, Returned: {returned}")
                return

        self.ui.textOutput.append("🚫 Book not found.")

    def list_books(self):
        self.load_data()
        self.ui.textOutput.clear()
        for title, book in self.library.items():
            status = "✅ Available" if book["available"] else f"❌ Borrowed by {book['borrower']}"
            self.ui.textOutput.append(f"{title} by {book['author']} — {status}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LibraryApp()
    window.setWindowTitle("Library 101 📚")
    window.show()
    sys.exit(app.exec())
