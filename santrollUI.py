# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'santrollUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.execlButton = QtWidgets.QPushButton(self.frame)
        self.execlButton.setMinimumSize(QtCore.QSize(0, 30))
        self.execlButton.setObjectName("execlButton")
        self.horizontalLayout.addWidget(self.execlButton)
        self.dataButton = QtWidgets.QPushButton(self.frame)
        self.dataButton.setMinimumSize(QtCore.QSize(0, 30))
        self.dataButton.setObjectName("dataButton")
        self.horizontalLayout.addWidget(self.dataButton)
        self.cleanPlotButton = QtWidgets.QPushButton(self.frame)
        self.cleanPlotButton.setMinimumSize(QtCore.QSize(0, 30))
        self.cleanPlotButton.setObjectName("cleanPlotButton")
        self.horizontalLayout.addWidget(self.cleanPlotButton)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plot1Button = QtWidgets.QPushButton(self.frame_2)
        self.plot1Button.setMinimumSize(QtCore.QSize(0, 30))
        self.plot1Button.setObjectName("plot1Button")
        self.horizontalLayout_2.addWidget(self.plot1Button)
        self.plot2Button = QtWidgets.QPushButton(self.frame_2)
        self.plot2Button.setMinimumSize(QtCore.QSize(0, 30))
        self.plot2Button.setObjectName("plot2Button")
        self.horizontalLayout_2.addWidget(self.plot2Button)
        self.plot3Button = QtWidgets.QPushButton(self.frame_2)
        self.plot3Button.setMinimumSize(QtCore.QSize(0, 30))
        self.plot3Button.setObjectName("plot3Button")
        self.horizontalLayout_2.addWidget(self.plot3Button)
        self.verticalLayout.addWidget(self.frame_2)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.verticalLayout.addWidget(self.table)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.execlButton.setText(_translate("MainWindow", "解析表格"))
        self.dataButton.setText(_translate("MainWindow", "数据"))
        self.cleanPlotButton.setText(_translate("MainWindow", "清除画图"))
        self.plot1Button.setText(_translate("MainWindow", "画图1"))
        self.plot2Button.setText(_translate("MainWindow", "画图2"))
        self.plot3Button.setText(_translate("MainWindow", "画图3"))
