import hashlib

class transaction():

	def __init__(self, sender, receiver, amount):
		self.sender = sender
		self.receiver = receiver
		self.amount = amount
		self.hashed_sender, self.hashed_receiver = self.hash_participants()

	def hash_participants(self):
		return hashlib.md5(str(self.sender).encode('ASCII')).hexdigest(), hashlib.md5(str(self.receiver).encode('ASCII')).hexdigest()

	def get_hashed_transaction_string(self):
		return f"{self.hashed_sender} > {self.hashed_receiver} ? 0x{self.amount:08X}"

	def get_transaction_string(self):
		return f"{self.sender.ljust(32)} > {self.receiver.ljust(34)} ? {self.amount:08d}"