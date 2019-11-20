from blockChain import *
from driver import *

class BlockChain:
    def __init__(self):
        self.blockchain = [create_genesis_block()]
        self.previous_block = self.blockchain[0]

    def addToBlockchain(self, data):
        addedBlock = next_block(self.previous_block, data)
        self.blockchain.append(addedBlock)
        newIndex = addedBlock.index
        self.previous_block = self.blockchain[newIndex]
