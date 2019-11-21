import datetime as date
import hashlib as hasher

from driver import *


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

    return Block(this_index, this_timestamp, this_data, this_hash)

def get_transaction_data(location, itemsPurchased, totalAmount, taxAmount, changeDealt, paymentMethod):
    this_data = [location, itemsPurchased, totalAmount, taxAmount, changeDealt, paymentMethod]

    return this_data