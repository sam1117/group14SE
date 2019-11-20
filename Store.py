

class Store:
    def __init__(self):
        #    inventory = {"item mane": [price, quantity], ... }
        self.inventory = {"jacket": [20.00, 10], "shirt": [7.00, 10], "pants": [9.00, 10], "shoes": [15.00, 10], "hat": [5.00, 10], "socks": [3.00, 10]}
        self.location = ""
        self.total = 0
        self.netTotal = 0
        self.taxPercentage = 0.07
        self.paymentMethod = []
        self.cartInProcess = []

    def setLocation(self, btnLocation):
        self.location = btnLocation

    def getLocation(self):
        return self.location

    def setPaymentMethod(self, paymentMethod):
        self.paymentMethod = paymentMethod
        print(self.paymentMethod)

    def getPaymentMethod(self):
        return self.paymentMethod

    def buildCart(self, cart):

        for i in range(len(cart)):
            itemName = cart[i][0]
            itemInfo = self.inventory.get(itemName)
            itemPrice = itemInfo[0]
            itemAvailable = itemInfo[1]
            quantityWanted = cart[i][1]

            if (itemAvailable >= quantityWanted):

                self.netTotal += (itemPrice * quantityWanted)
                self.cartInProcess.append([itemName, quantityWanted])

                newInventoryQuantity = (itemAvailable - quantityWanted)
                updatedInfo = [itemPrice, newInventoryQuantity]
                self.inventory[itemName] = updatedInfo

        self.total = (self.netTotal) + (self.netTotal * self.taxPercentage)


def purchase(location, paymentMethod, cart, netTotal, total):
    print("Implement later")