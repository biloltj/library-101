from PySide6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font_title = QtGui.QFont()
        font_title.setPointSize(16)
        font_title.setBold(True)

        self.labelTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(200, 10, 250, 40))
        self.labelTitle.setFont(font_title)
        self.labelTitle.setText("Library 101 📚")
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)

        self.labelPrompt = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelPrompt.setGeometry(QtCore.QRect(40, 60, 120, 30))
        self.labelPrompt.setText("Book Title:")

        self.inputTitle = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.inputTitle.setGeometry(QtCore.QRect(130, 60, 300, 30))

        self.btnSearch = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(450, 60, 100, 30))
        self.btnSearch.setText("Search")

        self.btnBorrow = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnBorrow.setGeometry(QtCore.QRect(40, 110, 100, 40))
        self.btnBorrow.setText("Borrow")

        self.btnReturn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnReturn.setGeometry(QtCore.QRect(160, 110, 100, 40))
        self.btnReturn.setText("Return")

        self.btnHistory = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnHistory.setGeometry(QtCore.QRect(280, 110, 100, 40))
        self.btnHistory.setText("Show History")

        self.btnListBooks = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnListBooks.setGeometry(QtCore.QRect(400, 110, 100, 40))
        self.btnListBooks.setText("List Books")

        self.btnExit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(250, 400, 100, 40))
        self.btnExit.setText("Exit")

        self.textOutput = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textOutput.setGeometry(QtCore.QRect(40, 170, 520, 210))
        self.textOutput.setReadOnly(True)

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
