"""
-interpolation.py
-this module interpolates a function with a set of inputs and outputs.
-this is based on lagrangian interpolation/lagrange multipliers
"""
import math 
import settings
import polynomial as pl 
import rational_expression as ratexp

with open(settings.INTERPOLATION_INPUT_PATH, "r") as input_file:
	inputs = [int(inp[:-1]) for inp in input_file.readlines()]

with open(settings.INTERPOLATION_OUTPUT_PATH, "r") as output_file:
	outputs = [int(out[:-1]) for out in output_file.readlines()]

def create_lj(j, inputs):

	lj =  ratexp.rational_exp(pl.polynomial([1]), pl.polynomial([1]))
	for i in range(len(inputs)):
		if i == j :
			continue;

		elif i != j:
			p1 = pl.polynomial([1, -inputs[i]])
			p2 = pl.polynomial([inputs[j] - inputs[i]])

			lj *= ratexp.rational_exp(p1, p2)

	return lj

def main():
	L = ratexp.rational_exp(pl.polynomial([1]), pl.polynomial([1]))
	for i in range(len(outputs)):
		L += create_lj(i, inputs) * ratexp.rational_exp(pl.polynomial([outputs[i]]), pl.polynomial([1]))
	#L.simplify()
	L.polys[0] -= pl.polynomial([1])
	#L.normalize()
	return L

#L = main();print(str(L), "\n", L(7))