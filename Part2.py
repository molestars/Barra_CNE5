# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\citics\Barra\code\Part2.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1311, 846)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(560, 20, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 190, 351, 535))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.calendar_start = QtWidgets.QCalendarWidget(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.calendar_start.setFont(font)
        self.calendar_start.setObjectName("calendar_start")
        self.verticalLayout_2.addWidget(self.calendar_start)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.calendar_end = QtWidgets.QCalendarWidget(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.calendar_end.setFont(font)
        self.calendar_end.setObjectName("calendar_end")
        self.verticalLayout_2.addWidget(self.calendar_end)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(440, 250, 122, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.factor_box = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.factor_box.setFont(font)
        self.factor_box.setObjectName("factor_box")
        self.factor_box.addItem("")
        self.factor_box.addItem("")
        self.factor_box.addItem("")
        self.factor_box.addItem("")
        self.factor_box.addItem("")
        self.factor_box.addItem("")
        self.factor_box.addItem("")
        self.factor_box.addItem("")
        self.factor_box.addItem("")
        self.factor_box.addItem("")
        self.verticalLayout_4.addWidget(self.factor_box)
        self.push_button = QtWidgets.QPushButton(self.centralwidget)
        self.push_button.setGeometry(QtCore.QRect(430, 620, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.push_button.setFont(font)
        self.push_button.setObjectName("push_button")
        self.label_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_pic.setGeometry(QtCore.QRect(620, 280, 661, 391))
        self.label_pic.setText("")
        self.label_pic.setObjectName("label_pic")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(840, 170, 331, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.halflife_box = QtWidgets.QTextEdit(self.centralwidget)
        self.halflife_box.setGeometry(QtCore.QRect(430, 470, 158, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.halflife_box.setFont(font)
        self.halflife_box.setObjectName("halflife_box")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(430, 419, 158, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1311, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "风险预测"))
        self.label_4.setText(_translate("MainWindow", "起始日"))
        self.label_6.setText(_translate("MainWindow", "截止日"))
        self.label_8.setText(_translate("MainWindow", "因子"))
        self.factor_box.setItemText(0, _translate("MainWindow", "Size"))
        self.factor_box.setItemText(1, _translate("MainWindow", "Beta"))
        self.factor_box.setItemText(2, _translate("MainWindow", "BTP"))
        self.factor_box.setItemText(3, _translate("MainWindow", "NLS"))
        self.factor_box.setItemText(4, _translate("MainWindow", "EY"))
        self.factor_box.setItemText(5, _translate("MainWindow", "Liquidity"))
        self.factor_box.setItemText(6, _translate("MainWindow", "Momentum"))
        self.factor_box.setItemText(7, _translate("MainWindow", "RV"))
        self.factor_box.setItemText(8, _translate("MainWindow", "Growth"))
        self.factor_box.setItemText(9, _translate("MainWindow", "Leverage"))
        self.push_button.setText(_translate("MainWindow", "导入"))
        self.label_9.setText(_translate("MainWindow", "因子风险预测效果"))
        self.label_10.setText(_translate("MainWindow", "预测半衰期"))
