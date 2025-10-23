import hashlib
import time

# Define a Block
class Block:
def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

# Generate Block Hash
def calculate_hash(index, previous_hash, timestamp, data):
value = str(index) + previous_hash + str(timestamp) + data
return hashlib.sha256(value.encode('utf-8')).hexdigest()

# Create the Blockchain
class Blockchain:
def __init__(self):
        self.chain = []
        self.create_genesis_block()

    # Create the first block (genesis block)
def create_genesis_block(self):
        genesis_block = Block(0, "0", time.time(), "Genesis Block", calculate_hash(0, "0", time.time(), "Genesis Block"))
self.chain.append(genesis_block)

    # Add a new block
def add_block(self, data):
        last_block = self.chain[-1]
        new_index = last_block.index + 1
        new_timestamp = time.time()
        new_hash = calculate_hash(new_index, last_block.hash, new_timestamp, data)
        new_block = Block(new_index, last_block.hash, new_timestamp, data, new_hash)
self.chain.append(new_block)

    # Print the Blockchain
def print_blockchain(self):
for block in self.chain:
print(f"Block #{block.index} [Hash: {block.hash}] - Data: {block.data}")

# Create Blockchain and add blocks
my_blockchain = Blockchain()
my_blockchain.add_block("Transaction 1")
my_blockchain.add_block("Transaction 2")

# Print the blockchain
my_blockchain.print_blockchain()
