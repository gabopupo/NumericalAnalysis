import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# utilitary function for function plotting
def dotplot(xi, yi, x, y, a, b):
    xi = np.array(xi).astype(np.int64)
    yi = np.array(yi).astype(np.int64)
    lf = sp.lambdify(x, y, modules=["numpy"])
    xval = np.linspace(a, b, 100)
    yval = lf(xval)

    plt.plot(xval, yval)
    plt.plot(xi, yi, 'ro')
    plt.show()

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
		divdif = sp.zeros(n, n)
		for i in range(n): # divdif[xi] = yi
			divdif[i,0] = yi[i]
		for j in range(n):
			w = 1 # product of (x - xi)
			for k in range(j):
				w *= (x-xi[k])
			for i in range(n-j-1): # compute every divided diffs of j-th order
				divdif[i,j+1] = (divdif[i+1,j] - divdif[i,j])/(xi[i+j+1] - xi[i])
			t = w*divdif[0,j]
			# verbose mode: show every computed term for Newton polynom
			if verb:
				print("\nt[%d] = " % j)
				sp.pprint(t)
				print("")
			y += t
	return y

