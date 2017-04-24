def union(a,b):
	return [la for la in a] + [lb for lb in b if lb not in a]

def intersect(a,b):
	return [la for la in a if la in b]

def sym_diff(a,b):
	return [la for la in a if la not in b] + [lb for lb in b if lb not in a]

def set_diff(a,b):
	return [la for la in a if la not in b]

def cart_prod(a,b):
	return [(a[i],b[i]) for i in range(len(a))]