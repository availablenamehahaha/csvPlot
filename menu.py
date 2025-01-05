import sys
from PyQt5.QtCore import Qt
import mainMenu
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QFont
import santrollMenu


class mainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.ui = mainMenu.Ui_MainWindow()
        self.ui.setupUi(self)
        self.uiInit()
        self.addConnect()
        self.santrollWin : santrollMenu.sanUI
        self.santrollWin = None

    def uiInit(self):
        self.ui.title.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(13)
        self.ui.title.setFont(font)
        self.setWindowTitle('画图软件')

    def addConnect(self):
        self.ui.SantrollButton.clicked.connect(self.openChildWindow)
        self.ui.CSVButton.clicked.connect(self.test)

    def openChildWindow(self):
        self.santrollWin = santrollMenu.sanUI()
        self.santrollWin.closed.connect(self.show)
        self.santrollWin.show()
        self.hide()

    def test(self):
        QMessageBox.information(self, 'CSV', '我还没写呢')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())
    # pyinstaller --onefile --windowed --icon=1.ico menu.py
