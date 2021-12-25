import hashlib
from block import block
from transaction import transaction
from blockchain import blockchain

if __name__ == "__main__":

	# Create some transactions
	t = []
	t.append(transaction("Jonas" , "Graham"  , 112))
	t.append(transaction("Graham" , "Joseph" , 115))
	t.append(transaction("Jack"   , "Patrick", 100))
	
	t2 = []
	t2.append(transaction("Patrick", "Steph"  , 42))
	t2.append(transaction("Steph"  , "Graham" , 8))
	t2.append(transaction("Marlene", "Jack"   , 1))

	#block(0, t, "0").show_hashed()

	graham_coin = blockchain()
	graham_coin.add_block(t)
	graham_coin.add_block(t2)
	
	graham_coin.show_hashed()