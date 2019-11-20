import datetime as date
import hashlib as hasher


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
        self.previous_block = 0

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(0, date.datetime.now(), ["Genesis Block"], "0")

def next_block(last_block, data):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = data
    this_hash = last_block.hash

    print(this_index, this_timestamp, this_data, this_hash) #TODO: dubugging purposes only, remove before submitting

    return Block(this_index, this_timestamp, this_data, this_hash)

def get_transaction_data(location, itemsPurchased, totalAmount, taxAmount, changeDealt, paymentMethod):
    this_data = [location, itemsPurchased, totalAmount, taxAmount, changeDealt, paymentMethod]

    return this_data


def search_by_id(chainToSearch, searchData): #searchData[index, timestamp, data[location, totalAmount, paymentMethod]]

    for i in range(len(chainToSearch)):
        block = chainToSearch[i]
        block_index = int(block.index)

        if (block_index == searchData):
            print("MATCH ON INDEX")
            print("INDEX:     " + str(block.index), searchData)
            break

        # else:
        #     print("NO BLOCK FOUND")

    print("Not found in blockchain")


def search_by_timestamp(chainToSearch, searchData):

    for i in range(len(chainToSearch)):
        block = chainToSearch[i]
        block_timestamp = str(block.timestamp)

        if (searchData in block_timestamp):
            print("MATCH ON TIMESTAMP")
            print("TIMESTAMP:     " + str(block.timestamp), searchData)
            break

        # else:
        #     print("NO BLOCK FOUND")

    print("Not found in blockchain")


def search_by_dataList(chainToSearch, location="default", totalAmount="default", paymentMethod="default"):

    for i in range(len(chainToSearch)):
        if (i == 0):
            continue

        block = chainToSearch[i]
        block_location = str(block.data[0])
        block_totalAmount = str(block.data[2])
        block_paymentMethod = str(block.data[5])

        if (block_location == location) or (block_totalAmount == totalAmount) or (block_paymentMethod == paymentMethod):
            return block

    print("Not found in blockchain")

def addNewBlock(self, transactionData):
    newTransactionData = get_transaction_data(transactionData)
    blocktoAdd = next_block(self.previous_block, newTransactionData)
    incrementChain = (self.previous_block + 1)
    previous_block = blockchain[incrementChain]

if __name__ == '__main__':
    # Create the blockchain and add the genesis block
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    newTransactionData = get_transaction_data("142 Wallaby Way Sydney, Australia", ["shirt", "shoes", "pants"], 134.41, 8.79, 0.00, "Credit: " + "Visa, " + str(123456789))
    blocktoAdd = next_block(previous_block, newTransactionData)
    blockchain.append(blocktoAdd)
    previous_block = blockchain[1]

    newTransactionData = get_transaction_data("100 Bulldog Blvd Starkville, MS", ["football", "cleats", "helmet"], 58123.58, 3802.48, (60000 - 58123.58), "Cash: " + str(60000))
    blocktoAdd = next_block(previous_block, newTransactionData)
    blockchain.append(blocktoAdd)
    previous_block = blockchain[2]

    newTransactionData = get_transaction_data("200 Bulldog Blvd Starkville, MS", ["football", "cleats", "helmet"], 58123.58, 3802.48, (60000 - 58123.58), "Cash: " + str(60000))
    blocktoAdd = next_block(previous_block, newTransactionData)
    blockchain.append(blocktoAdd)
    previous_block = blockchain[3]

    search_by_id(blockchain, 1)
    search_by_timestamp(blockchain, "2019-11-17")
    resultBlock = search_by_dataList(blockchain, "200 Bulldog Blvd Starkville, MS", "58123.58", "Cash: " + str(60000))
    print(resultBlock)