

class Store:
    def __init__(self):
        #    inventory = {"item mane": [price, quantity], ... }
        self.inventory = {"jacket": [20.00, 10], "shirt": [7.00, 10], "pants": [9.00, 10], "shoes": [15.00, 10], "hat": [5.00, 10], "socks": [3.00, 10]}
        self.location = ""
        self.paymentMethod = []
        self.total = 0
        self.netTotal = 0
        self.taxAmount = 0
        self.taxPercentage = 0.07
        self.cart = []

    def setLocation(self, btnLocation):
        self.location = btnLocation

    def getLocation(self):
        return self.location

    def setPaymentMethod(self, paymentMethod):
        self.paymentMethod = paymentMethod

    def getPaymentMethod(self):
        return self.paymentMethod

    def getTotal(self):
        return self.total

    def getNetTotal(self):
        return self.netTotal

    def getTaxAmount(self):
        return self.taxAmount

    def getTaxPercentage(self):
        return self.taxPercentage

    def setCart(self):
        self.cart = []

    def getCart(self):
        return self.cart

    def buildCart(self, cart):

        for i in range(len(cart)):
            itemName = cart[i][0]
            itemInfo = self.inventory.get(itemName)
            itemPrice = itemInfo[0]
            itemAvailable = itemInfo[1]
            quantityWanted = cart[i][1]

            if (itemAvailable >= quantityWanted):

                self.netTotal += (itemPrice * quantityWanted)
                self.cart.append([itemName, quantityWanted])

                newInventoryQuantity = (itemAvailable - quantityWanted)
                updatedInfo = [itemPrice, newInventoryQuantity]
                self.inventory[itemName] = updatedInfo

        self.taxAmount = round((self.netTotal * self.taxPercentage), 2)
        self.total = (self.netTotal + self.taxAmount)
