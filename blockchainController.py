from blockChain import *
from driver import *

class BlockChain:
    def __init__(self):
        self.blockchain = [create_genesis_block()]
        self.previous_block = self.blockchain[0]


    def addToBlockchain(self, data):
        try:
            self.addedBlock = next_block(self.previous_block, data)
            self.blockchain.append(self.addedBlock)
            newIndex = self.addedBlock.index
            self.previous_block = self.blockchain[newIndex]
            self.msgTransactionReceipt()

        except Exception as ex:
            print("Error adding to blockchain", ex)

    def search_by_id(self, searchID):

        try:
            block = self.blockchain[searchID]
            return block


        except Exception as ex:
            print("Nope!")


    def msgTransactionReceipt(self):
        transactionID = self.addedBlock.index
        transactionDate = self.addedBlock.timestamp
        transactionLocation = self.addedBlock.data[0]
        transactionItems = self.addedBlock.data[1]
        transactionNetTotal = self.addedBlock.data[2]
        transactionTaxAmount = self.addedBlock.data[3]
        transactionTotal = self.addedBlock.data[4]
        transactionPayMethod = self.addedBlock.data[5]
        transactionHash = self.addedBlock.hash

        itemDetail = ""
        for i in range(len(transactionItems)):
            name = transactionItems[i][0]
            quantity = str(transactionItems[i][1])
            itemDetail += name + ": \t" + quantity + "\n"

        paymentDetail = ""
        for i in range(len(transactionPayMethod)):
            print(transactionPayMethod[i], type(transactionPayMethod[i]))
            tmp = str(transactionPayMethod[i])

            if (i == 0):
                paymentDetail += tmp + ": "
            else:
                paymentDetail += tmp + "  "

        hashDetail = str(transactionHash)

        msg = QMessageBox()
        msg.setWindowTitle("Transaction Receipt")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Location: " + str(transactionLocation) + "\nTransactionID: " + str(transactionID) + "\nDate: " + str(transactionDate))
        msg.setInformativeText("Price:\n$" + str(transactionNetTotal) + "\nTax: $" + str(transactionTaxAmount) + "\nTotal: $" + str(transactionTotal))
        msg.setDetailedText("Items:\n--------------------\n" + itemDetail + "\nPayment Method:\n--------------------\n" + paymentDetail
                            + "\n\nHash:\n--------------------\n" + hashDetail)
        msg.exec()