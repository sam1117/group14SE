
inventory = {"jacket": 20, "shirt": 7.00, "pants": 9.00, "shoes": 15.00, "hat": 5.00, "socks": 3.00}

location = None
# netTotal = None
total    = 0
taxPercentage = 0.07    # 7% sales tax


def setLocation(btnLocation):
    location = btnLocation
    return location

def setPaymentMethod(paymentMethod):
    paymentMethod = paymentMethod
    return paymentMethod

def buildCart(cart, netTotal=0):

    for i in range(len(cart)):
        itemName = cart[i][0]
        itemPrice = inventory.get(itemName)
        itemQuantity = cart[i][1]

        netTotal = (netTotal) + (itemPrice * itemQuantity)

    total = (netTotal) + (netTotal * taxPercentage)
    return total, netTotal

def purchase(location, paymentMethod, cart, netTotal, total):
    print("Implement later")