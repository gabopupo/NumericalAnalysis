import sympy as sp
import sys
from numa import interpolate

def main():
	if len(sys.argv) < 2:
		print("Usage: interpolate.py <method> <verbose>\n\t<method>: -L (Lagrange), -N (Newton)\n\t<verbose>: -V (enable verbose solving)")
		exit(1)
	met = sys.argv[1].upper().replace("-", "")
	if len(sys.argv) > 2:
		verb = sys.argv[2].upper().replace("-", "")
	n = int(input("Number of pairs: "))
	xi = sp.zeros(n)
	yi = sp.zeros(n)
	x = sp.symbols("x")
	for i in range(int(n)):
		pair = input("Pair %d: " % (i+1)).split()
		xi[i], yi[i] = int(pair[0]), int(pair[1])
	y = interpolate(xi, yi, x, met, True if (len(sys.argv) > 2 and verb == "V") else False)
	print("Interpolated expression:")
	sp.pprint(sp.simplify(sp.factor(y)))

if __name__ == "__main__":
	main()