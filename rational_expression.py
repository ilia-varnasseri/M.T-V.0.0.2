"""
-rational_expressions.py
-this modules processes the rational expressions with the module <polynomial.py>
"""
import math
import polynomial as pl 
import graph_func as gr 
import number_theory as nt

class rational_exp(object):
	def __init__(self, p1, p2):
		self.polys = [p1, p2]

	def __call__(self, x):
		return self.polys[0](x) / self.polys[1](x)

	def __str__(self):
		return "(%s)/(%s)"%(str(self.polys[0]), str(self.polys[1]))

	def functionize(self):
		return lambda x : self(x)
	
	def simplify(self):
		n = math.gcd(self.polys[0].coeffs + self.polys[1].coeffs)#nt.gcd(self.polys[0].coeffs + self.polys[1].coeffs)
		self.polys = [pl.polynomial([i / n for i in self.polys[0].coeffs]), pl.polynomial([i / n for i in self.polys[1].coeffs])]
		return 1

	def normalize(self):
		self.polys[0].normalize()
		self.polys[1].normalize()

	def zeros(self):
		return self.polys[0].R()

	def undefined(self):
		return self.polys[1].R()

	def __add__(self, other):
		return rational_exp(self.polys[0] * other.polys[1] + other.polys[0] * self.polys[1], self.polys[1] * other.polys[1])

	def __sub__(self, other):
		return rational_exp(self.polys[0] * other.polys[1] - other.polys[0] * self.polys[1], self.polys[1] * other.polys[1])

	def __mul__(self, other):
		return rational_exp(self.polys[0] * other.polys[0], self.polys[1] * other.polys[1])

	def __div__(self, other):
		return self * other.reverse()

	def reverse(self):
		return rational_exp(self.polys[1], self.polys[0])

	def graph(self, f=[]):
		f.append(self)
		u = []
		for i in f:
			u += i.undefined()
		gr.plot(-100, 100, f, d=.01, exceptions=u[:])


