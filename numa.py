import sympy as sp

def interpolate(xi, yi, x, met, verb):
	n = xi.shape[0]
	y = 0 # interpolation polynom
	if met == "L":
		for i in range(n):
			l = 1 # Lagrange polynom
			for j in range(n):
				if i == j:
					continue
				l *= (x-xi[j])/(xi[i]-xi[j])
			# verbose mode: show every computed Lagrange polynom
			if verb:
				print("\nl[%d] = " % i)
				sp.pprint(l)
				print("")
			y += l*yi[i]
	if met == "N":
		print("TODO")
	return y

