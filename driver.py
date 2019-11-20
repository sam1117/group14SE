from PyQt5.QtWidgets import QMessageBox

from storeMain import *
from searchDialog import *
from blockchainController import  *
from Store import  *

# Create a store instance
store = Store()
blockChain = BlockChain()

def msgBoxPayment():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Purchase could not be completed")
    msg.setInformativeText("Payment information is incorrect or incomplete.")
    msg.setWindowTitle("Purchase not complete")
    msg.exec()

def checkOptions(self):
    locationSuccess = False
    buildCartSuccess = False
    paymentMethodSuccess = False
    tmppaymentMethod = []

    # Set the store location
    try:
        comboBoxText = str(self.comboBox.currentText())

        if (comboBoxText != ""):
            store.setLocation(comboBoxText)
            locationSuccess = True

    except Exception as ex:
        print("Error at location buttons: ", ex)

    # Set the items and quantities to purchase, then call buildCart
    store.setCart()
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
            tmpCart = []

    except Exception as ex:
        print("Error at item boxes: ", ex)

    try:
        cash_radioButton = self.cash_radioButton
        credit_radioButton = self.credit_radioButton
        check_radioButton = self.check_radioButton

        if cash_radioButton.isChecked():
            paymentMethodSelected = "cash"
            cash_lineEdit = self.cash_LineText
            if (cash_lineEdit.text() != ""):
                tmppaymentMethod.append(paymentMethodSelected)
                tmppaymentMethod.append(cash_lineEdit.text())

                store.setPaymentMethod(tmppaymentMethod)
                paymentMethodSuccess = True

            else:
                msgBoxPayment()

        if credit_radioButton.isChecked():
            paymentMethodSelected = "credit"
            creditName_lineEdit = self.creditName_lineEdit
            creditNumber_lineEdit = self.creditNumber_lineEdit
            creditCSV_lineEdit = self.creditCSV_lineEdit
            if (creditName_lineEdit.text() != "") and (creditNumber_lineEdit.text() != "") and (creditCSV_lineEdit.text() != ""):
                tmppaymentMethod.append(paymentMethodSelected)
                tmppaymentMethod.append(creditName_lineEdit.text())
                tmppaymentMethod.append(creditNumber_lineEdit.text())
                tmppaymentMethod.append(creditCSV_lineEdit.text())

                store.setPaymentMethod(tmppaymentMethod)
                paymentMethodSuccess = True

            else:
                msgBoxPayment()

        if check_radioButton.isChecked():
            paymentMethodSelected = "check"
            checkHolder_lineEdit = self.checkHolder_lineEdit
            checkAccount_lineEdit = self.checkAccount_lineEdit
            checkPayTo_lineEdit = self.checkPayTo_lineEdit
            checkAmount_lineEdit = self.checkAmount_lineEdit
            if (checkHolder_lineEdit.text() != "") and (checkAccount_lineEdit.text() != "") and (checkPayTo_lineEdit.text() != "") and (checkAmount_lineEdit.text()):
                tmppaymentMethod.append(paymentMethodSelected)
                tmppaymentMethod.append(checkHolder_lineEdit.text())
                tmppaymentMethod.append(checkAccount_lineEdit.text())
                tmppaymentMethod.append(checkPayTo_lineEdit.text())
                tmppaymentMethod.append(checkAmount_lineEdit.text())

                store.setPaymentMethod(tmppaymentMethod)
                paymentMethodSuccess = True

            else:
                msgBoxPayment()


    except Exception as ex:
        print("Error at payment method: ", ex)

    if (locationSuccess and buildCartSuccess and paymentMethodSuccess):
        transactionLocation = store.getLocation()
        transactionCart = store.getCart()
        transactionNetTotal = store.getNetTotal()
        transactionTaxAmount = store.getTaxAmount()
        transactionTotal = store.getTotal()
        transactionPaymentMethod = store.getPaymentMethod()

        transaction = [transactionLocation, transactionCart, transactionNetTotal, transactionTaxAmount, transactionTotal, transactionPaymentMethod]
        blockChain.addToBlockchain(transaction)
























