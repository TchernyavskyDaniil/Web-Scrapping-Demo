# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.tab_4)
        self.tabWidget.setMinimumSize(QtCore.QSize(100, 100))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 250, 96))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 38, 0, 38)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(280, 10, 401, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, 12, -1, 13)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_2.setStyleSheet("width: 160px;\n"
"\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lineEdit_2)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setStyleSheet("width: 160px;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_5.setStyleSheet("width:160px;")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lineEdit_5)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.horizontalLayout_5.addLayout(self.formLayout)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(260, 10, 20, 121))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget.addTab(self.tab, "")
        self.CSV = QtWidgets.QWidget()
        self.CSV.setObjectName("CSV")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.CSV)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.CSV)
        self.tableWidget.setMinimumSize(QtCore.QSize(300, 300))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.CSV, "")
        self.horizontalLayout_4.addWidget(self.tabWidget)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_5)
        self.tabWidget_3.setMinimumSize(QtCore.QSize(100, 100))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 251, 90))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_6.setContentsMargins(0, 37, 0, 33)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_6.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_6.addWidget(self.pushButton_5)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(280, 10, 401, 121))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_7.addWidget(self.pushButton_6)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(-1, 12, -1, 12)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_3.setStyleSheet("width: 160px;\n"
"\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lineEdit_3)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_4.setStyleSheet("width: 160px;\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lineEdit_4)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_6.setStyleSheet("width: 160px;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lineEdit_6)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.horizontalLayout_7.addLayout(self.formLayout_2)
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(260, 10, 20, 121))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tabWidget_3.addTab(self.tab_2, "")
        self.CSV_2 = QtWidgets.QWidget()
        self.CSV_2.setObjectName("CSV_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.CSV_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.CSV_2)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(300, 300))
        self.tableWidget_2.setStyleSheet("")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.horizontalLayout_8.addWidget(self.tableWidget_2)
        self.tabWidget_3.addTab(self.CSV_2, "")
        self.horizontalLayout_9.addWidget(self.tabWidget_3)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab_3)
        self.tabWidget_4.setMinimumSize(QtCore.QSize(100, 100))
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.tab_6)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 251, 96))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_10.setContentsMargins(0, 38, 0, 38)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_10.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_10.addWidget(self.pushButton_8)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.tab_6)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(280, 10, 401, 121))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_11.addWidget(self.pushButton_9)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setContentsMargins(-1, 43, -1, 13)
        self.formLayout_3.setObjectName("formLayout_3")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.lineEdit_9.setStyleSheet("width:160px;")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lineEdit_9)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_9)
        self.horizontalLayout_11.addLayout(self.formLayout_3)
        self.line_3 = QtWidgets.QFrame(self.tab_6)
        self.line_3.setGeometry(QtCore.QRect(260, 10, 20, 121))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.tabWidget_4.addTab(self.tab_6, "")
        self.CSV_3 = QtWidgets.QWidget()
        self.CSV_3.setObjectName("CSV_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.CSV_3)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.CSV_3)
        self.tableWidget_3.setMinimumSize(QtCore.QSize(300, 300))
        self.tableWidget_3.setStyleSheet("")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.horizontalLayout_12.addWidget(self.tableWidget_3)
        self.tabWidget_4.addTab(self.CSV_3, "")
        self.horizontalLayout_16.addWidget(self.tabWidget_4)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.tab_7)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.tabWidget_5 = QtWidgets.QTabWidget(self.tab_7)
        self.tabWidget_5.setMinimumSize(QtCore.QSize(100, 100))
        self.tabWidget_5.setObjectName("tabWidget_5")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.tab_8)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 20, 251, 90))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_13.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_13.setContentsMargins(0, 37, 0, 33)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_13.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_13.addWidget(self.pushButton_11)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.tab_8)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(280, 10, 401, 121))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButton_12 = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_14.addWidget(self.pushButton_12)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setContentsMargins(-1, 12, -1, 12)
        self.formLayout_4.setObjectName("formLayout_4")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_8)
        self.lineEdit_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_7.setStyleSheet("width: 160px;\n"
"\n"
"")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_8)
        self.lineEdit_8.setStyleSheet("width: 160px;\n"
"")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lineEdit_8)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_8)
        self.lineEdit_10.setStyleSheet("width: 160px;")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lineEdit_10)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_10)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_8.setObjectName("label_8")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_8)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_7)
        self.horizontalLayout_14.addLayout(self.formLayout_4)
        self.line_4 = QtWidgets.QFrame(self.tab_8)
        self.line_4.setGeometry(QtCore.QRect(260, 10, 20, 121))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.tabWidget_5.addTab(self.tab_8, "")
        self.CSV_4 = QtWidgets.QWidget()
        self.CSV_4.setObjectName("CSV_4")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.CSV_4)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.CSV_4)
        self.tableWidget_4.setMinimumSize(QtCore.QSize(300, 300))
        self.tableWidget_4.setStyleSheet("")
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.horizontalLayout_15.addWidget(self.tableWidget_4)
        self.tabWidget_5.addTab(self.CSV_4, "")
        self.horizontalLayout_17.addWidget(self.tabWidget_5)
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.tab_9)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.tabWidget_6 = QtWidgets.QTabWidget(self.tab_9)
        self.tabWidget_6.setMinimumSize(QtCore.QSize(100, 100))
        self.tabWidget_6.setObjectName("tabWidget_6")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.tab_10)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(10, 20, 251, 96))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_18.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_18.setContentsMargins(0, 38, 0, 38)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.pushButton_13 = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_18.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_18.addWidget(self.pushButton_14)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.tab_10)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(280, 10, 401, 121))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.pushButton_15 = QtWidgets.QPushButton(self.horizontalLayoutWidget_10)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_19.addWidget(self.pushButton_15)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setContentsMargins(-1, 43, -1, 13)
        self.formLayout_5.setObjectName("formLayout_5")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_10)
        self.lineEdit_11.setStyleSheet("width:160px;")
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lineEdit_11)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.label_11.setObjectName("label_11")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_11)
        self.horizontalLayout_19.addLayout(self.formLayout_5)
        self.line_5 = QtWidgets.QFrame(self.tab_10)
        self.line_5.setGeometry(QtCore.QRect(260, 10, 20, 121))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.tabWidget_6.addTab(self.tab_10, "")
        self.CSV_5 = QtWidgets.QWidget()
        self.CSV_5.setObjectName("CSV_5")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.CSV_5)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.CSV_5)
        self.tableWidget_5.setMinimumSize(QtCore.QSize(300, 300))
        self.tableWidget_5.setStyleSheet("")
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(0)
        self.tableWidget_5.setRowCount(0)
        self.horizontalLayout_20.addWidget(self.tableWidget_5)
        self.tabWidget_6.addTab(self.CSV_5, "")
        self.horizontalLayout_21.addWidget(self.tabWidget_6)
        self.tabWidget_2.addTab(self.tab_9, "")
        self.horizontalLayout_2.addWidget(self.tabWidget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_2.setObjectName("actionOpen_2")

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(4)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget_6.setCurrentIndex(0)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_5.clicked.connect(MainWindow.close)
        self.pushButton_8.clicked.connect(MainWindow.close)
        self.pushButton_11.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Open CSV"))
        self.pushButton_2.setText(_translate("MainWindow", "Quit"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.label.setText(_translate("MainWindow", "Password"))
        self.label_2.setText(_translate("MainWindow", "E-mail or Nickname"))
        self.label_5.setText(_translate("MainWindow", "Parse target"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CSV), _translate("MainWindow", "CSV Table"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Twitter"))
        self.pushButton_4.setText(_translate("MainWindow", "Open CSV"))
        self.pushButton_5.setText(_translate("MainWindow", "Quit"))
        self.pushButton_6.setText(_translate("MainWindow", "Start"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.label_4.setText(_translate("MainWindow", "E-mail or Nickname"))
        self.label_6.setText(_translate("MainWindow", "Parse target"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_2), _translate("MainWindow", "Main"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.CSV_2), _translate("MainWindow", "CSV Table"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Instagram"))
        self.pushButton_7.setText(_translate("MainWindow", "Open CSV"))
        self.pushButton_8.setText(_translate("MainWindow", "Quit"))
        self.pushButton_9.setText(_translate("MainWindow", "Start"))
        self.label_9.setText(_translate("MainWindow", "Parse target"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_6), _translate("MainWindow", "Main"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.CSV_3), _translate("MainWindow", "CSV Table"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "VK"))
        self.pushButton_10.setText(_translate("MainWindow", "Open CSV"))
        self.pushButton_11.setText(_translate("MainWindow", "Quit"))
        self.pushButton_12.setText(_translate("MainWindow", "Start"))
        self.label_10.setText(_translate("MainWindow", "Parse target"))
        self.label_8.setText(_translate("MainWindow", "E-mail or Nickname"))
        self.label_7.setText(_translate("MainWindow", "Password"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_8), _translate("MainWindow", "Main"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.CSV_4), _translate("MainWindow", "CSV Table"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "Linkendin"))
        self.pushButton_13.setText(_translate("MainWindow", "Open CSV"))
        self.pushButton_14.setText(_translate("MainWindow", "Quit"))
        self.pushButton_15.setText(_translate("MainWindow", "Start"))
        self.label_11.setText(_translate("MainWindow", "Parse target"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_10), _translate("MainWindow", "Main"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.CSV_5), _translate("MainWindow", "CSV Table"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("MainWindow", "BlackList"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen_2.setText(_translate("MainWindow", "Open"))
