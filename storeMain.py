# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mhhod\Desktop\group14SE\storeMain.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QTextEdit

from driver import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 692)
        MainWindow.setMouseTracking(False)
        MainWindow.setWindowFilePath("")
        MainWindow.setDocumentMode(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 40, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(190, 70, 521, 111))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cash_radioButton = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.cash_radioButton.setObjectName("cash_radioButton")
        self.verticalLayout_4.addWidget(self.cash_radioButton)
        self.credit_radioButton = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.credit_radioButton.setObjectName("credit_radioButton")
        self.verticalLayout_4.addWidget(self.credit_radioButton)
        self.check_radioButton = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.check_radioButton.setObjectName("check_radioButton")
        self.verticalLayout_4.addWidget(self.check_radioButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.cash_LineText = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.cash_LineText.setObjectName("cash_LineText")
        self.cash_LineText.setValidator(QDoubleValidator(0.01, 1000000.99, 2))             # Set check amount to only accept float
        self.verticalLayout_6.addWidget(self.cash_LineText)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.creditName_lineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.creditName_lineEdit.setObjectName("creditName_lineEdit")
        self.horizontalLayout_3.addWidget(self.creditName_lineEdit)
        self.creditNumber_lineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.creditNumber_lineEdit.setObjectName("creditNumber_lineEdit")
        self.creditNumber_lineEdit.setValidator(QIntValidator())                           # Set card number to only accept integers
        self.horizontalLayout_3.addWidget(self.creditNumber_lineEdit)
        self.creditCSV_lineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.creditCSV_lineEdit.setObjectName("creditCSV_lineEdit")
        self.creditCSV_lineEdit.setValidator(QIntValidator())                              # Set card CSV to only accept integers
        self.horizontalLayout_3.addWidget(self.creditCSV_lineEdit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkHolder_lineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.checkHolder_lineEdit.setText("")
        self.checkHolder_lineEdit.setObjectName("checkHolder_lineEdit")
        self.horizontalLayout_5.addWidget(self.checkHolder_lineEdit)
        self.checkAccount_lineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.checkAccount_lineEdit.setObjectName("checkAccount_lineEdit")
        self.checkAccount_lineEdit.setValidator(QIntValidator())                            # Set check account to only accept integers
        self.horizontalLayout_5.addWidget(self.checkAccount_lineEdit)
        self.checkPayTo_lineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.checkPayTo_lineEdit.setObjectName("checkPayTo_lineEdit")
        self.horizontalLayout_5.addWidget(self.checkPayTo_lineEdit)
        self.checkAmount_lineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.checkAmount_lineEdit.setObjectName("checkAmount_lineEdit")
        self.checkAmount_lineEdit.setValidator(QDoubleValidator(0.01, 1000000.99, 2))       # Set check amount to only accept float
        self.horizontalLayout_5.addWidget(self.checkAmount_lineEdit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 240, 84, 44))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_5.addWidget(self.comboBox)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(50, 40, 103, 178))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.shirt = QtWidgets.QCheckBox(self.layoutWidget1)
        self.shirt.setObjectName("shirt")
        self.verticalLayout_2.addWidget(self.shirt)
        self.pants = QtWidgets.QCheckBox(self.layoutWidget1)
        self.pants.setObjectName("pants")
        self.verticalLayout_2.addWidget(self.pants)
        self.shoes = QtWidgets.QCheckBox(self.layoutWidget1)
        self.shoes.setObjectName("shoes")
        self.verticalLayout_2.addWidget(self.shoes)
        self.hat = QtWidgets.QCheckBox(self.layoutWidget1)
        self.hat.setObjectName("hat")
        self.verticalLayout_2.addWidget(self.hat)
        self.socks = QtWidgets.QCheckBox(self.layoutWidget1)
        self.socks.setObjectName("socks")
        self.verticalLayout_2.addWidget(self.socks)
        self.jacket = QtWidgets.QCheckBox(self.layoutWidget1)
        self.jacket.setObjectName("jacket")
        self.verticalLayout_2.addWidget(self.jacket)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.shirt_spinBox = QtWidgets.QSpinBox(self.layoutWidget1)
        self.shirt_spinBox.setObjectName("shirt_spinBox")
        self.verticalLayout.addWidget(self.shirt_spinBox)
        self.pants_spinBox = QtWidgets.QSpinBox(self.layoutWidget1)
        self.pants_spinBox.setObjectName("pants_spinBox")
        self.verticalLayout.addWidget(self.pants_spinBox)
        self.shoes_spinBox = QtWidgets.QSpinBox(self.layoutWidget1)
        self.shoes_spinBox.setObjectName("shoes_spinBox")
        self.verticalLayout.addWidget(self.shoes_spinBox)
        self.hat_spinBox = QtWidgets.QSpinBox(self.layoutWidget1)
        self.hat_spinBox.setObjectName("hat_spinBox")
        self.verticalLayout.addWidget(self.hat_spinBox)
        self.socks_spinBox = QtWidgets.QSpinBox(self.layoutWidget1)
        self.socks_spinBox.setObjectName("socks_spinBox")
        self.verticalLayout.addWidget(self.socks_spinBox)
        self.jacket_spinBox = QtWidgets.QSpinBox(self.layoutWidget1)
        self.jacket_spinBox.setObjectName("jacket_spinBox")
        self.verticalLayout.addWidget(self.jacket_spinBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(480, 260, 239, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.purchase = QtWidgets.QPushButton(self.layoutWidget2)
        self.purchase.setObjectName("purchase")
        self.horizontalLayout_2.addWidget(self.purchase)
        self.quit = QtWidgets.QPushButton(self.layoutWidget2)
        self.quit.setObjectName("quit")
        self.horizontalLayout_2.addWidget(self.quit)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(50, 360, 301, 72))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.searchID_radioButton = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.searchID_radioButton.setObjectName("searchID_radioButton")
        self.verticalLayout_7.addWidget(self.searchID_radioButton)
        self.searchDate_radioButton = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.searchDate_radioButton.setObjectName("searchDate_radioButton")
        self.verticalLayout_7.addWidget(self.searchDate_radioButton)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setValidator(QIntValidator())                                          # Set search lineEdit to only accept integers
        self.verticalLayout_8.addWidget(self.lineEdit)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget_3)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())                      # Set default date to current system date
        self.verticalLayout_8.addWidget(self.dateEdit)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(470, 580, 119, 23))
        self.search.setObjectName("search")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 450, 541, 111))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)                                    # set textEdit not to wrap lines
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.quit.clicked.connect(MainWindow.close)
        self.purchase.clicked.connect(self.purchaseClicked)
        self.search.clicked.connect(self.searchClicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Payment Information"))
        self.cash_radioButton.setText(_translate("MainWindow", "Cash"))
        self.credit_radioButton.setText(_translate("MainWindow", "Credt Card"))
        self.check_radioButton.setText(_translate("MainWindow", "Check"))
        self.cash_LineText.setPlaceholderText(_translate("MainWindow", "$ Cash amount"))
        self.creditName_lineEdit.setPlaceholderText(_translate("MainWindow", "Card holder"))
        self.creditNumber_lineEdit.setPlaceholderText(_translate("MainWindow", "Card number"))
        self.creditCSV_lineEdit.setPlaceholderText(_translate("MainWindow", "Security code"))
        self.checkHolder_lineEdit.setPlaceholderText(_translate("MainWindow", "Account name"))
        self.checkAccount_lineEdit.setPlaceholderText(_translate("MainWindow", "Account number"))
        self.checkPayTo_lineEdit.setPlaceholderText(_translate("MainWindow", "Pay to"))
        self.checkAmount_lineEdit.setPlaceholderText(_translate("MainWindow", "Check amount"))
        self.label_3.setText(_translate("MainWindow", "Store Location"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Starkville"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Jackson"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Memphis"))
        self.label.setText(_translate("MainWindow", "Inventory"))
        self.shirt.setText(_translate("MainWindow", "shirt"))
        self.pants.setText(_translate("MainWindow", "pants"))
        self.shoes.setText(_translate("MainWindow", "shoes"))
        self.hat.setText(_translate("MainWindow", "hat"))
        self.socks.setText(_translate("MainWindow", "socks"))
        self.jacket.setText(_translate("MainWindow", "jacket"))
        self.purchase.setText(_translate("MainWindow", "Purchase"))
        self.quit.setText(_translate("MainWindow", "Quit"))
        self.label_4.setText(_translate("MainWindow", "Search Type"))
        self.searchID_radioButton.setText(_translate("MainWindow", "Search by TransactionID"))
        self.searchDate_radioButton.setText(_translate("MainWindow", "Search by Transaction Date"))
        self.label_5.setText(_translate("MainWindow", "Search Criteria"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Transaction id..."))
        self.search.setText(_translate("MainWindow", "Search"))

    def purchaseClicked(self):
        checkOptions(self)

    def searchClicked(self):
        checkSearchFields(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
