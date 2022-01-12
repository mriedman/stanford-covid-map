mm=lambda x,y:x*x+x*y+y*y
def karat(x,y):
	print(x,y)
	if len(str(x)) == 1 or len(str(y)) == 1: return mm(x,y)
	b = len(str(x))//2
	a,bb,c,d = int(str(x)[:b]), int(str(x)[b:]), int(str(y)[:b]), int(str(y)[b:])
	z1, z2, z3 = karat(a,c), karat(bb,d), karat(a+bb,c+d)
	return 10**(2*b)*z1+10**b*(z3-z1-z2)+z2
print(karat(1234,4321))
