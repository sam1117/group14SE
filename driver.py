import datetime as date
import hashlib as hasher


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

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

def getTransactionData(location, itemsPurchased, totalAmount, taxAmount, changeDealt, paymentMethod):
    this_data = [location, itemsPurchased, totalAmount, taxAmount, changeDealt, paymentMethod]

    return this_data


if __name__ == '__main__':
    # Create the blockchain and add the genesis block
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    a = getTransactionData("142 Wallaby Way Sydney, Australia", ["shirt", "shoes", "pants"], 134.41, 8.79, 0.00, "Credit: " + "Visa, " + str(123456789))
    b = next_block(previous_block, a)
    previous_block = b

    c = getTransactionData("100 Bulldog Blvd Starkville, MS", ["football", "cleats", "helmet"], 58123.58, 3802.48, (60000 - 58123.58), "Cash: " + str(60000))
    d = next_block(previous_block, c)
    previous_block = d
