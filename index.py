import hashlib
import time

# Step 1: Define the Block Structure
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        #Calculate the hash of the block
        data_to_hash = ( str(self.index) + str(self.timestamp) + str(self.data) + self.previous_hash + str(self.nonce) )
        return hashlib.sha256(data_to_hash.encode()).hexdigest()

    def mine_block(self, difficulty):
        #Perform proof of work
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

# Step 2: Create Genesis Block
def create_genesis_block():
    """Generate the genesis (first) block."""
    return Block(0, time.time(), "Genesis Block", "0")

# Step 3: Develop the Blockchain Class
class Blockchain:
    def __init__(self):
        self.chain = [create_genesis_block()]
        self.difficulty = 4  # Adjustable difficulty level

    def get_latest_block(self):
        #Retrieve the latest block in the chain
        return self.chain[-1]

    def add_block(self, new_block):
        #Add a new block to the chain after mining
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        #Verify the integrity of the blockchain
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check hash integrity
            if current_block.hash != current_block.calculate_hash():
                print("Invalid block hash")
                return False

            # Check hash linkage
            if current_block.previous_hash != previous_block.hash:
                print("Invalid chain linkage")
                return False

        return True

# Step 4: Mining and Adding Blocks
def main():
    # Initialize blockchain
    my_blockchain = Blockchain()

    # Add new blocks
    print("Mining block 1...")
    my_blockchain.add_block(Block(1, time.time(), "Block 1 Data", my_blockchain.get_latest_block().hash))

    print("Mining block 2...")
    my_blockchain.add_block(Block(2, time.time(), "Block 2 Data", my_blockchain.get_latest_block().hash))

    print("Mining block 3...")
    my_blockchain.add_block(Block(3, time.time(), "Block 3 Data", my_blockchain.get_latest_block().hash))

    # Display the blockchain
    for block in my_blockchain.chain:
        print(f"Block {block.index}:")
        print(f"  Timestamp: {time.ctime(block.timestamp)}")
        print(f"  Data: {block.data}")
        print(f"  Previous Hash: {block.previous_hash}")
        print(f"  Hash: {block.hash}")
        print(f"  Nonce: {block.nonce}\n")

    # Validate the blockchain
    print("Is blockchain valid?", my_blockchain.is_chain_valid())

if __name__ == "__main__":
    main()
