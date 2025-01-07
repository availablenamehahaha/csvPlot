import sys
from PyQt5.QtCore import Qt
import mainMenu
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QFont
import santrollMenu
import plot_func


class mainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.ui = mainMenu.Ui_MainWindow()
        self.ui.setupUi(self)
        self.uiInit()
        self.addConnect()
        self.santrollWin : santrollMenu.sanUI
        self.santrollWin = None
        self.CSVWin : plot_func.PlotUi
        self.CSVWin = None

    def uiInit(self):
        self.ui.title.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(13)
        self.ui.title.setFont(font)
        self.setWindowTitle('画图软件')

    def addConnect(self):
        self.ui.SantrollButton.clicked.connect(self.openSantrollWindow)
        self.ui.CSVButton.clicked.connect(self.openCSVWindow)

    def openSantrollWindow(self):
        self.santrollWin = santrollMenu.sanUI()
        self.santrollWin.closed.connect(self.show)
        self.santrollWin.show()
        self.hide()

    def openCSVWindow(self):
        # QMessageBox.information(self, 'CSV', '我还没写呢')
        self.CSVWin = plot_func.PlotUi()
        self.CSVWin.closed.connect(self.show)
        self.CSVWin.show()
        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())
    # pyinstaller --onefile --windowed --icon=1.ico menu.py
