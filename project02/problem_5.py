#!/usr/bin/env python3

import hashlib
from time import time, ctime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = ctime(timestamp)
        self.data = data
        self.previous_hash = previous_hash
        self.hash = Block._calc_hash(self.data, self.timestamp)
        self.ref = None

    def __repr__(self):
        return f"""
                Block []: Data: {repr(self.data)}
                Hash: {repr(self.hash)}
                Previous Hash: {repr(self.previous_hash)}
                {repr(self.timestamp)}
        """

    @staticmethod
    def _calc_hash(data, timestamp):
        """
        Creates a SHA-256 hash of a block with data and timestamp

        args:
        data - String
        timestamp - Datetime
        """
        sha = hashlib.sha256()
        # Feed bytes to SHA256 hash object
        sha.update(data.encode())
        sha.update(timestamp.encode())

        return sha.hexdigest()


class BlockChain:
    def __init__(self, genesis_block=True):
        self.last = None
        # add Genesis Block by default
        if genesis_block:
            self.add_first_block()

    def add_first_block(self):
        """
        Adds genesis block(first block) to block chain
        
        """
        if self.last is not None:
            print("Blockchain already has its first block")
            return
        else:
            self.last = BlockChain._create_genesis_block()

    def add_block(self, data):
        """
        Adds block to block chain 
        
        args:
        data 
        """

        new_block = Block(time(), data, self.last.hash)
        new_block.ref = self.last
        self.last = new_block

    @staticmethod
    def _create_genesis_block():
        "Creates a genesis block, the first block of a block chain"

        return Block(time(), "Genesis Block", None)

    def __repr__(self):
        curr = self.last
        res = ""
        if curr is None:
            return "Blockchain is empty!"

        else:
            while curr is not None:

                res += repr(curr)
                if curr is not None:
                    res += "\n"
                curr = curr.ref

            return res


print("Test Cases:")
chain = BlockChain()
print(chain)

for n in range(3):
    chain.add_block(str(n))

print(chain)
