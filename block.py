from datetime import datetime
import hashlib
import random
import colorama
from transaction import transaction
from colorama import Fore, Back

# https://developer.bitcoin.org/reference/block_chain.html
class block():
	""" Block of blockchain
		The block contains 4 main elements:
		nonce - Number only used once
		txs   - A list of transactions
		previous_hash - The hash of the previous block
		time_stamp - The actual date and time
		merkle - Hash of list of transactions in my case
	"""

	def __init__(self, index, txs, previous_hash):
		colorama.init()
		self.index = index
		self.txs = txs
		self.previous_hash = previous_hash
		self.time_stamp = datetime.now()
		self.nonce = random.randint(0, 2**32)
		self.merkle = self.get_merkle()
		self.hash = self.get_hash()

	def get_hash(self):
		"""
			Compute the hash of the block and return it
		"""
		return hashlib.sha256(str(self.index).encode('ASCII')
							+ str(self.merkle).encode('ASCII')
							+ str(self.previous_hash).encode('ASCII')
							+ str(self.time_stamp).encode('ASCII')
							+ str(self.nonce).encode('ASCII')).hexdigest()

	def get_merkle(self):
		"""
			No Real merkle made with tree for now, might implement it later
		"""
		return hashlib.sha256(str(self.txs).encode('ASCII')).hexdigest()

	def show_hashed(self):
		print(f"\n\n{Fore.YELLOW}----------------------------------------- BLOCK {self.index} -----------------------------------------")

		print(f"Block number : {self.index}")
		print(f"Block hash   : {self.hash}")
		print(f"Merkle hash  : {self.merkle}")
		print(f"Previous hash: {self.previous_hash}")
		print(f"Time stamp   : {self.time_stamp}")
		print(f"Nonce        : {self.nonce}")

		print(f"{Fore.MAGENTA}####################################### TRANSACTIONS ######################################")
		print("--- ID ---", end=" ")
		print("------------ SENDER ------------", end="   ")
		print("----------- RECEIVER -----------", end="   ")
		print("- AMOUNT -")
		for i, transaction in enumerate(self.txs):
			print(f"0x{i:08X} {transaction.get_hashed_transaction_string()}")
	
	def show(self):
		print(f"\n\n{Fore.YELLOW}----------------------------------------- BLOCK {self.index} -----------------------------------------")

		print(f"Block number : {self.index}")
		print(f"Block hash   : {self.hash}")
		print(f"Merkle hash  : {self.merkle}")
		print(f"Previous hash: {self.previous_hash}")
		print(f"Time stamp   : {self.time_stamp}")
		print(f"Nonce        : {self.nonce}")

		print(f"{Fore.MAGENTA}####################################### TRANSACTIONS ######################################")
		print("--- ID ---", end=" ")
		print("------------ SENDER ------------", end="   ")
		print("----------- RECEIVER -----------", end="   ")
		print("- AMOUNT -")
		for i, transaction in enumerate(self.txs):
			print(f"0x{i:08X} {transaction.get_transaction_string()}")

