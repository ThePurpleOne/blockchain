import block
import hashlib
from transaction import transaction

if __name__ == "__main__":

	# Create some transactions
	t = []
	t.append(transaction("Jonas" , "Graham"  , 112))
	t.append(transaction("Graham" , "Joseph" , 115))
	t.append(transaction("Jack"   , "Patrick", 100))
	t.append(transaction("Patrick", "Steph"  , 42))
	t.append(transaction("Steph"  , "Graham" , 8))
	t.append(transaction("Marlene", "Jack"   , 1))

	# Create a new block
	block_1 = block.block(1, t, hashlib.sha256("0".encode('ASCII')).hexdigest())
	block_1.show_hashed()
	block_1.show()
