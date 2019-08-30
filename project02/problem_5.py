#!/usr/bin/env python3

import hashlib
from time import time, ctime, sleep


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = ctime(timestamp)
        self.data = data
        self.previous_hash = previous_hash
        self.hash = Block._calc_hash(self.data, self.timestamp)
        self.ref = None

    def __repr__(self):
        return (
            f"Block []: {repr(self.data)}\n"
            f"Hash: {repr(self.hash)}\n"
            f"Previous Hash: {repr(self.previous_hash)}\n"
            f"{repr(self.timestamp)}\n"
        )

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
        # Adds genesis block(first block) to block chain

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


print("TestCase 0: Init Blockchain with Genesis Block by default:")
chain = BlockChain()
print(chain)
"""
Block []: 'Genesis Block'
Hash: [HASH]
Previous Hash: None
[DATE]

"""

print("TestCase 1: Add another block")
chain.add_block("Hello World!")
print(chain)
"""
Block []: 'Hello World!'
Hash: [HASH]
Previous Hash: [HASH of Genesis Block]
[DATE]

Block []: 'Genesis Block'
Hash: [HASH]
Previous Hash: None
'Fri Aug 30 14:36:07 2019'
"""
print("TestCase 2: Add 10 Blocks")

for n in range(10):
    chain.add_block(str(n))

print(chain)

"""
Block []: '9'
Hash: [HASH]
Previous Hash: [HASH of Genesis Block]
[DATE]

--Abbreviated ----


Block []: 'Genesis Block'
Hash: [HASH]
Previous Hash: None
[DATE]

"""
