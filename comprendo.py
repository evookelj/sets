def union(a,b):
	return [la for la in a] + [lb for lb in b if lb not in a]

def intersect(a,b):
	return [la for la in a if la in b]

def set_diff(a,b):
	pass

def sym_diff(a,b):
	pass

def cart_prod(a,b):
	pass