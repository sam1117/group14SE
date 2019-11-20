# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mhhod\Desktop\group14SE\storeMain.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Store import *

store = Store()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(742, 381)
        MainWindow.setMouseTracking(False)
        MainWindow.setDocumentMode(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 40, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 60, 101, 154))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.shirt = QtWidgets.QCheckBox(self.layoutWidget)
        self.shirt.setObjectName("shirt")
        self.verticalLayout_2.addWidget(self.shirt)

        self.pants = QtWidgets.QCheckBox(self.layoutWidget)
        self.pants.setObjectName("pants")
        self.verticalLayout_2.addWidget(self.pants)

        self.shoes = QtWidgets.QCheckBox(self.layoutWidget)
        self.shoes.setObjectName("shoes")
        self.verticalLayout_2.addWidget(self.shoes)

        self.hat = QtWidgets.QCheckBox(self.layoutWidget)
        self.hat.setObjectName("hat")
        self.verticalLayout_2.addWidget(self.hat)

        self.socks = QtWidgets.QCheckBox(self.layoutWidget)
        self.socks.setObjectName("socks")
        self.verticalLayout_2.addWidget(self.socks)

        self.jacket = QtWidgets.QCheckBox(self.layoutWidget)
        self.jacket.setObjectName("jacket")
        self.verticalLayout_2.addWidget(self.jacket)

        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.shirt_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.shirt_spinBox.setObjectName("shirt_spinBox")
        self.verticalLayout.addWidget(self.shirt_spinBox)

        self.pants_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.pants_spinBox.setObjectName("pants_spinBox")
        self.verticalLayout.addWidget(self.pants_spinBox)

        self.shoes_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.shoes_spinBox.setObjectName("shoes_spinBox")
        self.verticalLayout.addWidget(self.shoes_spinBox)

        self.hat_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.hat_spinBox.setObjectName("hat_spinBox")
        self.verticalLayout.addWidget(self.hat_spinBox)

        self.socks_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.socks_spinBox.setObjectName("socks_spinBox")
        self.verticalLayout.addWidget(self.socks_spinBox)

        self.jacket_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.jacket_spinBox.setObjectName("jacket_spinBox")
        self.verticalLayout.addWidget(self.jacket_spinBox)

        self.horizontalLayout.addLayout(self.verticalLayout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(310, 60, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.credit_payment = QtWidgets.QRadioButton(self.centralwidget)
        self.credit_payment.setGeometry(QtCore.QRect(180, 90, 82, 17))
        self.credit_payment.setObjectName("credit_payment")

        self.purchase = QtWidgets.QPushButton(self.centralwidget)
        self.purchase.setGeometry(QtCore.QRect(250, 200, 75, 23))
        self.purchase.setObjectName("purchase")

        self.check_payment = QtWidgets.QRadioButton(self.centralwidget)
        self.check_payment.setGeometry(QtCore.QRect(180, 120, 82, 17))
        self.check_payment.setObjectName("check_payment")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 40, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.cash_payment = QtWidgets.QRadioButton(self.centralwidget)
        self.cash_payment.setGeometry(QtCore.QRect(180, 60, 82, 17))
        self.cash_payment.setObjectName("cash_payment")

        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(330, 200, 75, 23))
        self.cancel.setObjectName("cancel")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.purchase.clicked.connect(self.checkOptions)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Store Location"))
        self.shirt.setText(_translate("MainWindow", "shirt"))
        self.pants.setText(_translate("MainWindow", "pants"))
        self.shoes.setText(_translate("MainWindow", "shoes"))
        self.hat.setText(_translate("MainWindow", "hat"))
        self.socks.setText(_translate("MainWindow", "socks"))
        self.jacket.setText(_translate("MainWindow", "jacket"))
        self.label.setText(_translate("MainWindow", "Inventory"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Starkville"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Jackson"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Memphis"))
        self.credit_payment.setText(_translate("MainWindow", "Credit"))
        self.purchase.setText(_translate("MainWindow", "Purchase"))
        self.check_payment.setText(_translate("MainWindow", "Check"))
        self.label_2.setText(_translate("MainWindow", "Payment Method"))
        self.cash_payment.setText(_translate("MainWindow", "Cash"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))

    def layout_widgets(layout):
        return (layout.itemAt(i) for i in range(layout.count()))

    def checkOptions(self):
        locationSuccess = False
        buildCartSuccess = False
        paymentMethodSuccess = False
        paymentMethodSelected = ""

        # location = ""
        # netTotal = 0
        # Total = 0

        # Get the store location
        try:
            comboBoxText = str(self.comboBox.currentText())

            if (comboBoxText != ""):
                store.setLocation(comboBoxText)
                locationSuccess = True

            # starkville_location = self.starkville_location
            # jackson_location = self.jackson_location
            # memphis_location = self.memphis_location
            #
            # if starkville_location.isChecked():
            #     location = setLocation("Starkville_Location")
            #
            # if jackson_location.isChecked():
            #     location = setLocation("Jackson_Location")
            #
            # if memphis_location.isChecked():
            #     location = setLocation("Memphis_Location")

        except Exception as ex:
            print("Error at location buttons: ", ex)

        # Get the items and quantities to purchase, then call buildCart
        try:
            tmpCart = []
            if self.hat.isChecked():
                item = "hat"
                quantity = self.hat_spinBox.value()
                tmpCart.append([item, quantity])
                print(tmpCart)

            if self.jacket.isChecked():
                item = "jacket"
                quantity = self.jacket_spinBox.value()
                tmpCart.append([item, quantity])
                print(tmpCart)

            if self.pants.isChecked():
                item = "pants"
                quantity = self.pants_spinBox.value()
                tmpCart.append([item, quantity])
                print(tmpCart)

            if self.shirt.isChecked():
                item = "shirt"
                quantity = self.shirt_spinBox.value()
                tmpCart.append([item, quantity])
                print(tmpCart)

            if self.shoes.isChecked():
                item = "shoes"
                quantity = self.shoes_spinBox.value()
                tmpCart.append([item, quantity])
                print(tmpCart)

            if self.socks.isChecked():
                item = "socks"
                quantity = self.socks_spinBox.value()
                tmpCart.append([item, quantity])
                print(tmpCart)

            if (len(tmpCart) != 0):
                store.buildCart(tmpCart)
                buildCartSuccess = True

        except Exception as ex:
            print("Error at item boxes: ", ex)

        # Get payment method
        try:
            cash_payment = self.cash_payment
            credit_payment = self.credit_payment
            check_payment = self.check_payment

            if cash_payment.isChecked():
                paymentMethodSelected = "cash"
                paymentMethodSuccess = True

            if credit_payment.isChecked():
                paymentMethodSelected = "credit"
                paymentMethodSuccess = True

            if check_payment.isChecked():
                paymentMethodSelected = "check"
                paymentMethodSuccess = True

        except Exception as ex:
            print("Error at payment method: ", ex)


        if (locationSuccess and buildCartSuccess and paymentMethodSuccess):
            print("\n", locationSuccess, buildCartSuccess, paymentMethodSuccess, "\n")





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
