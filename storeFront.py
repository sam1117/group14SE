# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mhhod\Desktop\group14SE\storeFront.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from driver import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(722, 300)
        self.purchase = QtWidgets.QPushButton(Dialog)
        self.purchase.setGeometry(QtCore.QRect(210, 170, 75, 23))
        self.purchase.setObjectName("purchase")

        self.cancel = QtWidgets.QPushButton(Dialog)
        self.cancel.setGeometry(QtCore.QRect(290, 170, 75, 23))
        self.cancel.setObjectName("cancel")

        self.starkville_location = QtWidgets.QRadioButton(Dialog)
        self.starkville_location.setGeometry(QtCore.QRect(160, 40, 111, 17))
        self.starkville_location.setObjectName("starkville_location")
        # self.starkville_location.toggled.connect(self.onClickedRadioBtn)

        self.jackson_location = QtWidgets.QRadioButton(Dialog)
        self.jackson_location.setGeometry(QtCore.QRect(160, 70, 111, 17))
        self.jackson_location.setObjectName("jackson_location")
        # self.jackson_location.toggled.connect(self.onClickedRadioBtn)

        self.memphis_location = QtWidgets.QRadioButton(Dialog)
        self.memphis_location.setGeometry(QtCore.QRect(160, 100, 111, 17))
        self.memphis_location.setObjectName("memphis_location")
        # self.memphis_location.toggled.connect(self.onClickedRadioBtn)

        self.cash_payment = QtWidgets.QRadioButton(Dialog)
        self.cash_payment.setGeometry(QtCore.QRect(310, 40, 82, 17))
        self.cash_payment.setObjectName("cash_payment")

        self.credit_payment = QtWidgets.QRadioButton(Dialog)
        self.credit_payment.setGeometry(QtCore.QRect(310, 70, 82, 17))
        self.credit_payment.setObjectName("credit_payment")

        self.check_payment = QtWidgets.QRadioButton(Dialog)
        self.check_payment.setGeometry(QtCore.QRect(310, 100, 82, 17))
        self.check_payment.setObjectName("check_payment")

        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 40, 101, 154))
        self.widget.setObjectName("widget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.shirt = QtWidgets.QCheckBox(self.widget)
        self.shirt.setObjectName("shirt")
        self.verticalLayout_2.addWidget(self.shirt)

        self.pants = QtWidgets.QCheckBox(self.widget)
        self.pants.setObjectName("pants")
        self.verticalLayout_2.addWidget(self.pants)

        self.shoes = QtWidgets.QCheckBox(self.widget)
        self.shoes.setObjectName("shoes")
        self.verticalLayout_2.addWidget(self.shoes)

        self.hat = QtWidgets.QCheckBox(self.widget)
        self.hat.setObjectName("hat")
        self.verticalLayout_2.addWidget(self.hat)

        self.socks = QtWidgets.QCheckBox(self.widget)
        self.socks.setObjectName("socks")
        self.verticalLayout_2.addWidget(self.socks)

        self.jacket = QtWidgets.QCheckBox(self.widget)
        self.jacket.setObjectName("jacket")
        self.verticalLayout_2.addWidget(self.jacket)

        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.shirt_spinBox = QtWidgets.QSpinBox(self.widget)
        self.shirt_spinBox.setObjectName("shirt_spinBox")
        self.verticalLayout.addWidget(self.shirt_spinBox)

        self.pants_spinBox = QtWidgets.QSpinBox(self.widget)
        self.pants_spinBox.setObjectName("pants_spinBox")
        self.verticalLayout.addWidget(self.pants_spinBox)

        self.shoes_spinBox = QtWidgets.QSpinBox(self.widget)
        self.shoes_spinBox.setObjectName("shoes_spinBox")
        self.verticalLayout.addWidget(self.shoes_spinBox)

        self.hat_spinBox = QtWidgets.QSpinBox(self.widget)
        self.hat_spinBox.setObjectName("hat_spinBox")
        self.verticalLayout.addWidget(self.hat_spinBox)

        self.socks_spinBox = QtWidgets.QSpinBox(self.widget)
        self.socks_spinBox.setObjectName("socks_spinBox")
        self.verticalLayout.addWidget(self.socks_spinBox)

        self.jacket_spinBox = QtWidgets.QSpinBox(self.widget)
        self.jacket_spinBox.setObjectName("jacket_spinBox")
        self.verticalLayout.addWidget(self.jacket_spinBox)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.purchase.clicked.connect(self.checkOptions)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.purchase.setText(_translate("Dialog", "Purchase"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.starkville_location.setText(_translate("Dialog", "Starkville Location"))
        self.jackson_location.setText(_translate("Dialog", "Jackson Location"))
        self.memphis_location.setText(_translate("Dialog", "Memphis Location"))
        self.cash_payment.setText(_translate("Dialog", "Cash"))
        self.credit_payment.setText(_translate("Dialog", "Credit"))
        self.check_payment.setText(_translate("Dialog", "Check"))
        self.shirt.setText(_translate("Dialog", "shirt"))
        self.pants.setText(_translate("Dialog", "pants"))
        self.shoes.setText(_translate("Dialog", "shoes"))
        self.hat.setText(_translate("Dialog", "hat"))
        self.socks.setText(_translate("Dialog", "socks"))
        self.jacket.setText(_translate("Dialog", "jacket"))

    def layout_widgets(layout):
        return (layout.itemAt(i) for i in range(layout.count()))

    def checkOptions(self):
        location = ""
        paymentMethod = ""
        cart = []
        netTotal = 0
        Total = 0

        # Get the store location
        try:
            starkville_location = self.starkville_location
            jackson_location = self.jackson_location
            memphis_location = self.memphis_location

            if starkville_location.isChecked():
                location = setLocation("Starkville_Location")

            if jackson_location.isChecked():
                location = setLocation("Jackson_Location")

            if memphis_location.isChecked():
                location = setLocation("Memphis_Location")

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
                cart = tmpCart
                total, netTotal = buildCart(tmpCart)

        except Exception as ex:
            print("Error at item boxes: ", ex)

        # Get payment method
        try:
            cash_payment = self.cash_payment
            credit_payment = self.credit_payment
            check_payment = self.check_payment

            if cash_payment.isChecked():
                paymentMethod = setPaymentMethod("cash")

            if credit_payment.isChecked():
                paymentMethod = setPaymentMethod("credit")

            if check_payment.isChecked():
                paymentMethod = setPaymentMethod("check")

        except Exception as ex:
            print("Error at payment method: ", ex)

        else:
            purchase(location, paymentMethod, cart, netTotal, total)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
