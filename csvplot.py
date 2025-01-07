# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 540)
        MainWindow.setMaximumSize(QtCore.QSize(360, 540))
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/launch/images/toolbox_launch_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lab_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lab_title.setFont(font)
        self.lab_title.setObjectName("lab_title")
        self.gridLayout.addWidget(self.lab_title, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.list_in = QtWidgets.QListWidget(self.centralwidget)
        self.list_in.setObjectName("list_in")
        self.gridLayout.addWidget(self.list_in, 2, 0, 6, 1)
        self.list_out = QtWidgets.QListWidget(self.centralwidget)
        self.list_out.setAcceptDrops(False)
        self.list_out.setObjectName("list_out")
        self.gridLayout.addWidget(self.list_out, 2, 1, 1, 1)
        self.btn_xt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_xt.setFont(font)
        self.btn_xt.setObjectName("btn_xt")
        self.gridLayout.addWidget(self.btn_xt, 3, 1, 1, 1)
        self.btn_xy = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_xy.setFont(font)
        self.btn_xy.setObjectName("btn_xy")
        self.gridLayout.addWidget(self.btn_xy, 4, 1, 1, 1)
        self.btn_xyz = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_xyz.setFont(font)
        self.btn_xyz.setObjectName("btn_xyz")
        self.gridLayout.addWidget(self.btn_xyz, 5, 1, 1, 1)
        self.btn_export = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_export.setFont(font)
        self.btn_export.setObjectName("btn_export")
        self.gridLayout.addWidget(self.btn_export, 6, 1, 1, 1)
        self.lab_encode = QtWidgets.QLabel(self.centralwidget)
        self.lab_encode.setObjectName("lab_encode")
        self.gridLayout.addWidget(self.lab_encode, 7, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CSV画图"))
        self.lab_title.setText(_translate("MainWindow", "拖放csv文件"))
        self.label.setText(_translate("MainWindow", "数据列表"))
        self.label_2.setText(_translate("MainWindow", "绘制项"))
        self.btn_xt.setText(_translate("MainWindow", "X-T"))
        self.btn_xy.setText(_translate("MainWindow", "X-Y"))
        self.btn_xyz.setText(_translate("MainWindow", "X-Y-Z"))
        self.btn_export.setText(_translate("MainWindow", "常用图像生成"))
        self.lab_encode.setText(_translate("MainWindow", "TextLabel"))
