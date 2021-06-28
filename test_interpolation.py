import sys
import settings
import graph_func as gr 
import interpolation as inter
import polynomial as pl 


F = pl.polynomial([1, -1]) * pl.polynomial([1, -15]) * pl.polynomial([1, 4])  #f = lambda x : (x - 1) * (x - 15) * (x + 4) 

def create_string(array):
	arr = ["%d\n"%(x) for x in array]
	string = "".join(arr)
	return string

inputs = list(range(6)); in_array = create_string(inputs)
outputs = [F(x) for x in inputs] ; out_array = create_string(outputs)

with open(settings.INTERPOLATION_INPUT_PATH, "w") as file:
	file.write(in_array)
	file.close()

with open(settings.INTERPOLATION_OUTPUT_PATH, "w") as file:
	file.write(out_array)
	file.close()

L = inter.main(); print(str(L))
L.graph(f=[F])
#gr.plot(-100, 100, f)

#print(L(int(sys.argv[1])) - 1);
