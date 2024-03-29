import datetime

from PyQt5.QtWidgets import QMessageBox

from storeMain import *
from blockchainController import  *
from Store import  *


# Create a store instance
store = Store()
blockChain = BlockChain()

def msgBoxPayment():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Purchase could not be completed")
    msg.setInformativeText("Information is incorrect or incomplete.")
    msg.setWindowTitle("Purchase not complete")
    msg.exec()

def msgBoxSearch():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Search could not be completed")
    msg.setInformativeText("Search field is incorrect or incomplete.")
    msg.setWindowTitle("Search not complete")
    msg.exec()

def msgBoxNoResult():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("No results found")
    msg.setInformativeText("Index does not exist.")
    msg.setWindowTitle("Search complete")
    msg.exec()

def checkSearchFields(self):
    searchField_id = 0
    searchField_date = datetime.date(2001, 1, 1)
    searchDone = False

    try:
        if (not self.searchID_radioButton.isChecked()) and (not self.searchDate_radioButton.isChecked()):
            pass

        if (self.searchID_radioButton.isChecked()) and (self.lineEdit.text() != ""):
            searchField_id = int(self.lineEdit.text())

            result = blockChain.search_by_id(searchField_id)
            receiptFromIDSearch(self, result)
            searchDone = True

        if (self.searchDate_radioButton.isChecked()) and (self.dateEdit.date() != ""):
            qt_date = self.dateEdit.date()

            result = blockChain.search_by_date(qt_date)
            receiptFromDateSearch(self, result)

            searchDone = True

        if (searchDone == False):
            msgBoxSearch()

    except Exception as ex:
        print("Error at search buttons: ", ex)
        msgBoxSearch()

def receiptFromDateSearch(self, blockList):

    if (len(blockList) == 0):
        msgBoxNoResult()

    try:
        self.textEdit.clear()

        for index in range(len(blockList)):
            resultID = blockList[index].index
            resultDate = blockList[index].timestamp
            resultLocation = blockList[index].data[0]
            resultItems = blockList[index].data[1]
            resultNetTotal = blockList[index].data[2]
            resultTaxAmount = blockList[index].data[3]
            resultTotal = blockList[index].data[4]
            resultPayMethod = blockList[index].data[5]
            resultHash = blockList[index].hash

            header = "ID\tDate\t\tLocation"
            header2 = "\nNet Total\tTax\tTotal\tPayment Method"
            header3 = "\nItems"
            header4 = "\nHash"

            resultStr = ("\n" + str(resultID) + "\t" + str(resultDate) + "\t" + str(resultLocation) + "\n")
            resultStr2 = ("\n" + str(resultNetTotal) + "\t" + str(resultTaxAmount) + "\t" + str(resultTotal) + "\t" + str(resultPayMethod) + "\n")
            resultStr3 = ("\n" + str(resultItems) + "\n")
            resultStr4 = ("\n" + str(resultHash) + "\n")

            self.textEdit.append(header + resultStr + header2 + resultStr2 + header3 + resultStr3 + header4 + resultStr4)
            self.textEdit.append("\n-----------------------------------------------------------------------------------------------------------------------------\n")

    except Exception as ex:
        msgBoxNoResult()

def receiptFromIDSearch(self, block):

    try:
        resultID = block.index
        resultDate = block.timestamp
        resultLocation = block.data[0]
        resultItems = block.data[1]
        resultNetTotal = block.data[2]
        resultTaxAmount = block.data[3]
        resultTotal = block.data[4]
        resultPayMethod = block.data[5]
        resultHash = block.hash

        header = "ID\tDate\t\tLocation"
        header2 = "\nNet Total\tTax\tTotal\tPayment Method"
        header3 = "\nItems"
        header4 = "\nHash"

        resultStr = ("\n" + str(resultID) + "\t" + str(resultDate) + "\t" + str(resultLocation) + "\n")
        resultStr2 = ("\n" + str(resultNetTotal) + "\t" + str(resultTaxAmount) + "\t" + str(resultTotal) + "\t" + str(resultPayMethod) + "\n")
        resultStr3 = ("\n" + str(resultItems) + "\n")
        resultStr4 = ("\n" + str(resultHash) + "\n")

        self.textEdit.clear()
        self.textEdit.setText(header + resultStr + header2 + resultStr2 + header3 + resultStr3 + header4 + resultStr4)
        self.textEdit.append("\n-----------------------------------------------------------------------------------------------------------------------------\n")

    except Exception as ex:
        msgBoxNoResult()

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
    store.setCart()     # clear previous items from cart
    try:
        tmpCart = []
        if self.hat.isChecked():
            item = "hat"
            quantity = self.hat_spinBox.value()
            tmpCart.append([item, quantity])

        if self.jacket.isChecked():
            item = "jacket"
            quantity = self.jacket_spinBox.value()
            tmpCart.append([item, quantity])

        if self.pants.isChecked():
            item = "pants"
            quantity = self.pants_spinBox.value()
            tmpCart.append([item, quantity])

        if self.shirt.isChecked():
            item = "shirt"
            quantity = self.shirt_spinBox.value()
            tmpCart.append([item, quantity])

        if self.shoes.isChecked():
            item = "shoes"
            quantity = self.shoes_spinBox.value()
            tmpCart.append([item, quantity])

        if self.socks.isChecked():
            item = "socks"
            quantity = self.socks_spinBox.value()
            tmpCart.append([item, quantity])

        if (len(tmpCart) != 0):
            store.buildCart(tmpCart)
            buildCartSuccess = True
            tmpCart = []

    except Exception as ex:
        print("Error at item boxes: ", ex)

    # Set the payment method and information
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

    else:
        msgBoxPayment()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Group 14 Point of Service")
    MainWindow.show()
    sys.exit(app.exec_())























