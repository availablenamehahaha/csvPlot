import sys
import santrollUI
import re
import pandas as pd
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidgetItem, QMessageBox, QWidget
from PyQt5.QtCore import pyqtSignal
from ExeclRule import ruleListAdd, patternDict
from main import transRule
from plot import dataPlot


class sanUI(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(sanUI, self).__init__(parent)
        self.ui = santrollUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.addConnect()
        self.UIInit()
        self.ruleList = []
        self.tableTitle = []
        self.oldDataSave = ""
        self.plotData = None
        self.tableInit = False

    def addConnect(self):
        self.ui.execlButton.clicked.connect(self.loadExcel)
        self.ui.table.cellChanged.connect(self.itemChanged)
        self.ui.table.itemDoubleClicked.connect(self.tableItemSaveOldData)
        self.ui.dataButton.clicked.connect(self.selectData)
        self.ui.cleanPlotButton.clicked.connect(self.cleanPlot)
        self.ui.plot1Button.clicked.connect(self.plotNum1)
        self.ui.plot2Button.clicked.connect(self.plotNum2)
        self.ui.plot3Button.clicked.connect(self.plotNum3)

    def UIInit(self):
        self.setWindowTitle('sanroll')

    def loadExcel(self):
        # 打开文件对话框选择 Excel 文件
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "选择 Excel 文件", "",
                                                   "Excel Files (*.xlsx *.xls);;All Files (*)", options=options)

        # file_name = 'example.xlsx'
        if file_name:
            df = pd.read_excel(file_name)
            self.ruleList = ruleListAdd(df)
            # 设置表格的行数和列数
            self.ui.table.setRowCount(len(df))
            self.ui.table.setColumnCount(len(df.columns))
            # 设置表格的列标题
            for col in range(len(df.columns)):
                self.ui.table.setHorizontalHeaderItem(col, QTableWidgetItem(df.columns[col]))
            # 填充表格数据
            for row in range(len(df)):
                for col in range(len(df.columns)):
                    self.ui.table.setItem(row, col, QTableWidgetItem(str(df.iat[row, col])))
            self.tableInit = True

    def itemChanged(self, row, column):
        # print(f"行数:{row}列数:{column}")
        head = self.ui.table.horizontalHeaderItem(column).text()
        self.tableItemCheck(row, column, patternDict.get(head))
        if self.tableInit:
            rule: transRule
            rule = self.ruleList[row]
            value = self.ui.table.item(row, column).text()
            if head == 'Name':
                rule.name = value
            elif head == 'ID':
                rule.ID = value
            elif head == 'First':
                rule.begin = int(value)
            elif head == 'Bits':
                rule.bits = int(value)
            elif head == 'Signed':
                rule.signed = bool(int(value))
            elif head == 'Pu':
                rule.pu = float(value)
            elif head == 'Offset':
                rule.offset = float(value)
            elif head == 'intel':
                rule.intel = bool(int(value))
            elif head == 'Color':
                rule.color = value
            print(rule)

    def tableItemSaveOldData(self, item):
        item: QTableWidgetItem
        self.oldDataSave = item.text()

    def tableItemCheck(self, row, column, pattern):
        item = self.ui.table.item(row, column)
        match = re.match(pattern, item.text())
        if match is None:
            item.setText(self.oldDataSave)
        head = self.ui.table.horizontalHeaderItem(column).text()
        if head == 'ID':
            strTemp = item.text().upper()
            strTemp = strTemp.zfill(8)
            item.setText(strTemp)

    def selectData(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "选择 txt 文件", "",
                                                   "Excel Files (*.txt);;All Files (*)", options=options)
        try:
            self.plotData = dataPlot(file_name)
        except:
            QMessageBox.warning(self, '警告', '数据导入失败')

    def cleanPlot(self):
        column_index = 1
        row_count = self.ui.table.rowCount()
        for row in range(row_count):
            item = self.ui.table.item(row, column_index)
            item.setText('0')

    def plotDraw(self, num: str):
        column_index = 1
        row_count = self.ui.table.rowCount()
        drawRuleList = []
        for row in range(row_count):
            item = self.ui.table.item(row, column_index)
            if item:
                data = item.text()
                if data == num:
                    drawRuleList.append(self.ruleList[row])
        if not drawRuleList:
            QMessageBox.warning(self, '警告', '未选择数据')
            return
        if not self.plotData:
            QMessageBox.warning(self, '警告', '未导入数据')
            return
        self.plotData.lineDraw(drawRuleList)

    def plotNum1(self):
        self.plotDraw('1')

    def plotNum2(self):
        self.plotDraw('2')

    def plotNum3(self):
        self.plotDraw('3')

    def closeEvent(self, event):
        super().closeEvent(event)
        self.closed.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = sanUI()
    window.show()
    sys.exit(app.exec_())
