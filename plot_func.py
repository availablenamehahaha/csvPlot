#encoding=utf8
import copy
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
import sys
import re
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import *
from matplotlib.font_manager import FontProperties

from load_csv import LoadCsvFile
from csvplot import *

# 设置 Matplotlib 的字体
# plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']  # 或者使用其他已安装的中文字体
# plt.rcParams['axes.unicode_minus'] = False  # 确保负号'-'显示正常

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题


class PlotUi(QMainWindow, Ui_MainWindow):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(PlotUi, self).__init__(parent)
        self.setupUi(self)
        self.file_name_ = ''
        self.lab_encode.setText('')
        self.btn_export.hide()
        '''连接信号槽函数'''
        self.btn_xt.clicked.connect(self.OnBtnXT)
        self.btn_xy.clicked.connect(self.OnBtnXT)
        self.btn_xyz.clicked.connect(self.OnBtnXT)
        self.btn_export.clicked.connect(self.OnBtnExport)
        self.list_in.clicked.connect(self.OnListInClick)
        self.list_out.clicked.connect(self.OnListOutClick)
        # 常用图像列表
        self.arglist = ['俯仰角', '横滚角', 'dvl前速', '航向角', '目标航向', '主压力传感器', '目标深度', '左舵目标',
                        '左舵反馈']
        self.figure = []
        for i in range(0, 3, 1):
            self.figure.append(self.arglist[i:i + 1])
        for i in range(3, len(self.arglist), 2):
            self.figure.append(self.arglist[i:i + 2])

    def dragEnterEvent(self, event):
        """拖拽对象到可操作窗口时触发"""
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                local_file_path = url.toLocalFile()  # 尝试获取本地文件路径
                if local_file_path:
                    filename = local_file_path
                    self.csv_th = LoadCsvFile(filename)
                    self.csv_th.start()  # 开启加载csv的Qt线程
                    self.csv_th.trigger.connect(self.OnUpdateProcess)  # 连接槽函数
                    self.pd = QProgressDialog(self)  # 进度对话框
                    self.pd.setWindowTitle("csv")
                    self.pd.setLabelText("加载进度")
                    self.pd.setRange(0, 100)
                    self.pd.setCancelButtonText(None)
                    self.pd.show()
                    self.csv = self.csv_th
        else:
            event.ignore()
        pass

    def OnUpdateProcess(self, msg):
        """更新加载进度"""
        if msg == 'load finish':
            try:
                #计算时间间隔
                l = self.csv_th.GetDataFrame()[u'时间']
                if len(l) < 100:
                    QMessageBox.warning(self, '警告', '数据量过少', QMessageBox.Yes, QMessageBox.Yes)
                    return
                t1 = l[0]
                t2 = l[99]
                obj = re.search(r'.*:(.*)', t1)
                if obj:
                    line_time = self.calculate_time_difference(t1, t2) * 1000 / 100
                    print(line_time)
                    # line_time = abs(float(t2)-float(t1))*50
                    if line_time > 80 and line_time < 120:
                        self.line_time = 100
                    elif line_time > 180 and line_time < 220:
                        self.line_time = 200
                    elif line_time > 800 and line_time < 1200:
                        self.line_time = 1000
                    else:
                        self.line_time = 1000
                else:
                    s2 = str(t2).split('_')
                    s1 = str(t1).split('_')
                    if len(s2) == 2 and len(s1) == 2:
                        self.line_time = float(int(s2[1]) - int(s1[1])) / 5.0
            except Exception as e:
                print(e)
                self.line_time = 100
            #显示处理结果
            self.OnShowResults()
            pass
        else:  #更新加载进度
            val = float(msg.replace('process:', ''))
            val = val * 100
            self.pd.setValue(int(val))

    def calculate_time_difference(self, timestamp1, timestamp2):
        format_str = '%Y-%m-%d_%H:%M:%S.%f'
        dt1 = datetime.strptime(timestamp1, format_str)
        dt2 = datetime.strptime(timestamp2, format_str)
        time_difference = dt2 - dt1
        return int(time_difference.total_seconds())

    def OnShowResults(self):
        """显示处理结果"""
        self.list_in.clear()
        self.list_out.clear()
        #加载标题名
        head = self.csv_th.GetDataFrame().columns
        for val in head.tolist():
            self.list_in.addItem(val)  # 列出数据列表（csv标题列表）

    def OnListInClick(self):
        """加载绘制项列表"""
        find_flag = False
        for i in range(self.list_out.count()):
            if self.list_out.item(i).text() == self.list_in.currentItem().text():
                find_flag = True
                break
        if not find_flag:
            self.list_out.addItem(self.list_in.currentItem().text())  # 添加item到out框

    def OnListOutClick(self):
        self.list_out.takeItem(self.list_out.currentRow())  # 删除out当前的item

    def OnBtnExport(self):
        if self.list_in.count() < 1:
            QMessageBox.warning(self, '提示', '请先加载文件', QMessageBox.Yes, QMessageBox.Yes)
        else:
            df = self.csv_th.GetDataFrame()
            figure = copy.deepcopy(self.figure)
            if figure != []:  # 创建子图
                fig, ax = plt.subplots(2, 3)
                for i in range(len(figure)):
                    args = figure.pop(0)
                    for arg in args:
                        results = self.list_in.findItems(arg, Qt.MatchContains)
                        if results:
                            result = results[0].text()
                            l = df[result]
                            ax[i // 3][i % 3].grid(True)
                            ax[i // 3][i % 3].plot(l, label=result)
                            x_lab = u'时间{}ms'.format(self.line_time)
                            ax[i // 3][i % 3].set_xlabel(x_lab)
                            ax[i // 3][i % 3].legend()
                plt.suptitle(self.file_name_)
                plt.show()

    def OnBtnXT(self):
        if self.list_out.count() < 1:
            QMessageBox.warning(self, '提示', '请选择索引', QMessageBox.Yes, QMessageBox.Yes)
        else:  #判断是否存在数据
            df = self.csv_th.GetDataFrame()
            if self.sender().objectName() == 'btn_xt':
                fig = plt.figure()
                ax = plt.axes()
                ax.grid()
                x_lab = u'时间{}ms'.format(self.line_time)
                ax.set_xlabel(x_lab)
                for i in range(self.list_out.count()):
                    l = df[self.list_out.item(i).text()]
                    ax.plot(l, label=self.list_out.item(i).text())
                ax.legend()
                plt.title(self.file_name_)
                plt.show()
            elif self.sender().objectName() == 'btn_xy':
                if self.list_out.count() % 2 != 0:
                    QMessageBox.warning(self, '提示', '必须双列', QMessageBox.Yes, QMessageBox.Yes)
                    return
                try:
                    fig = plt.figure()
                    ax = plt.axes()
                    ax.grid()
                    for i in range(0, self.list_out.count(), 2):
                        if self.list_out.item(i).text() == "时间" or self.list_out.item(i + 1).text() == "时间":
                            QMessageBox.warning(self, '警告', '请勿选择时间项', QMessageBox.Yes, QMessageBox.Yes)
                            return
                        lx = df[self.list_out.item(i).text()]
                        ly = df[self.list_out.item(i + 1).text()]
                        lx_o = []
                        ly_o = []
                        for lx_1 in lx.tolist():
                            if lx_1 != 0:
                                lx_o.append(lx_1)
                        for ly_1 in ly.tolist():
                            if ly_1 != 0:
                                ly_o.append(ly_1)
                        ax.set_xlabel(self.list_out.item(i).text())
                        ax.set_ylabel(self.list_out.item(i + 1).text())
                        ax.plot(lx_o, ly_o)
                    ax.legend()
                    plt.show()
                except:
                    pass
            elif self.sender().objectName() == 'btn_xyz':
                if self.list_out.count() != 3:
                    QMessageBox.warning(self, '提示', '只允许选择三项索引')
                    return
                fig = plt.figure()
                ax = fig.add_subplot(projection='3d')  # 新版matplotlib将gca改为add_subplot
                plt.grid()
                for i in range(0, self.list_out.count(), 3):
                    if self.list_out.item(i).text() == "时间" or \
                            self.list_out.item(i + 1).text() == "时间" or \
                            self.list_out.item(i + 2).text() == "时间":
                        QMessageBox.warning(self, '警告', '请勿选择时间项', QMessageBox.Yes, QMessageBox.Yes)
                        return
                    lx = df[self.list_out.item(i).text()]
                    ly = df[self.list_out.item(i + 1).text()]
                    lz = df[self.list_out.item(i + 2).text()]
                    lz = -lz
                ax.plot(lx, ly, lz)
                plt.show()
                pass

    def closeEvent(self, event):
        super().closeEvent(event)
        self.closed.emit()


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


if __name__ == "__main__":
    #print ('total,',datetime.datetime.now() - start)
    app = QApplication(sys.argv)
    ui = PlotUi()
    ui.show()
    sys.exit(app.exec_())
