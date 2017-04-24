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

a = [1,3,5,7,9]
b = [0,2,4,6,8]
c = union(a,b)
print "c = union [1,3,5,7,9] and [0,2,4,6,8] = %s"%(str(c))

d = intersect(b,c)
print "d = intersection [0,2,4,6,8] and c = %s"%(str(d))

#e = 