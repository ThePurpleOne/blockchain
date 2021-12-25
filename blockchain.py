from block import block
from transaction import transaction

class blockchain():
	"""[summary]

	Returns:
		[type]: [description]
	"""


	def __init__(self):
		self.chain = [self.create_genesis_block()]
		self.index = 0

	def create_genesis_block(self):
		genesis_transaction = []
		genesis_transaction.append(transaction('0', '0', 0))
		return block(0, genesis_transaction, f"{0:064x}")

	def add_block(self, transactions):
		self.index += 1
		new_block = block(self.index, transactions, self.chain[-1].hash)
		self.chain.append(new_block)

	def is_valid(self):
		for i in len(self.chain):
			crt_block = self.chain[i]
			pvs_block = self.chain[i-1]

			# Check if Hash stored in current block is correct
			if current_block.hash != current_block.get_hash():
				return False

			# Check if previous block's hash stored in current block is correct	
			if current_block.previous_hash != previous_block.hash:
				return False

		# Everything seems valid
		return True

	def show_hashed(self):
		for block in self.chain:
			block.show_hashed()

	def show(self):
		for block in self.chain:
			print(block.show())