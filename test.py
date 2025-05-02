from library import load_library, save_library
from datetime import datetime, timedelta
def welcome():
    print("📚✨ Welcome to Library 101 ✨📚")
    print("Your personal assistant for managing library books! 💡")
    print("-----------------------------------------------------")
def main_menu():
    print("\n📘 What would you like to do?")
    print("1. 🔍 Search for a book")
    print("2. 📖 Borrow a book")
    print("3. 📤 Return a book")
    print("4. 🕓 View borrowing history")
    print("5. 📚 List all books")
    print("6. ❌ Exit")

    choice = input("Enter the number of your choice: ")
    return choice
def main():
    welcome()
    global library
    library = load_library()

    
    while True:
        choice = main_menu()

        if choice == "1":
            search_book()
        elif choice == "2":
            borrow_book()

        elif choice == "3":
            return_book()

        elif choice == "4":
            view_history()

        elif choice == "5":
            list_books()

        elif choice == "6":
            print("👋 Goodbye! Thanks for visiting Library 101.")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 6.")
def search_book():
    search_query = input("🔍 Enter the title or part of the title to search: ").lower()
    found = False

    print("\n📖 Search Results:")
    for title, details in library.items():
        if search_query in title.lower():
            status = "✅ Available" if details["available"] else f"❌ Borrowed by {details['borrower']}"
            print(f"- {title} by {details['author']} — {status}")
            found = True

    if not found:
        print("🚫 No books matched your search.")
def borrow_book():
    title = input("📖 Enter the title of the book you want to borrow: ").strip()

    if title not in library:
        print("🚫 Book not found in the library.")
        return

    book = library[title]

    if not book["available"]:
        print(f"❌ Sorry, '{title}' is currently borrowed by {book['borrower']}.")
        return

    borrower = input("🙋‍♀️ Enter your name: ").strip()
    due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")

    book["available"] = False
    book["borrower"] = borrower
    book["due_date"] = due_date
    book["history"].append((borrower, datetime.now().strftime("%Y-%m-%d"), None))
    
    save_library(library)
    print(f"✅ Success! '{title}' has been borrowed by {borrower}. Due back on {due_date}.")
def return_book():
    title = input("📤 Enter the title of the book you want to return: ").strip()

    if title not in library:
        print("🚫 Book not found in the library.")
        return

    book = library[title]

    if book["available"]:
        print(f"ℹ️ '{title}' is already available in the library.")
        return

    return_date = datetime.now().strftime("%Y-%m-%d")

    book["available"] = True
    borrower = book["borrower"]
    book["borrower"] = None
    book["due_date"] = None

    if book["history"]:
        last_entry = book["history"][-1]
        if last_entry[2] is None:
            book["history"][-1] = (last_entry[0], last_entry[1], return_date)
    save_library(library)

    print(f"✅ '{title}' has been successfully returned by {borrower}. Thank you!")

def view_history():
    title = input("🕓 Enter the title of the book to view history: ").strip()

    if title not in library:
        print("🚫 Book not found in the library.")
        return

    book = library[title]
    history = book["history"]

    if not history:
        print(f"ℹ️ No borrowing history found for '{title}'.")
        return

    print(f"\n📚 Borrowing History for '{title}':")
    print("👤 Borrower | 📅 Borrowed On | 📅 Returned On")
    print("---------------------------------------------")
    for entry in history:
        borrower, borrowed_on, returned_on = entry
        returned_text = returned_on if returned_on else "⏳ Not returned yet"
        print(f"{borrower:<12} | {borrowed_on}     | {returned_text}")

def list_books():
    print("\n📚 All Books in Library 101:")
    print("📖 Title | ✍️ Author | 📦 Status")
    print("---------------------------------------------")

    for title, info in library.items():
        author = info["author"]
        status = "✅ Available" if info["available"] else f"❌ Borrowed by {info['borrower']}"
        print(f"{title:<20} | {author:<20} | {status}")

if __name__ == "__main__":
    main()
