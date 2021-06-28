import matplotlib.pyplot as plt 

def spectrum(start, end, d):
	rn = []
	for i in range(start, end + 1):
		j = 0
		while j < 1:
			rn.append(i + j)
			j += d

	return rn

def plot(start, end, functions, d=.01, exceptions = []):
	def plot_single_func(func):
		xf = []
		yf = []
		for i in spectrum(start, end, d):
			if i not in exceptions:
				xf.append(i)
				yf.append(func(i))

		return xf, yf
	Df = []
	Xs = []
	Ys = []
	for F in functions:
		x, y = plot_single_func(F)
		Df.append((x, y))
		Xs += x; Ys += y

	min_x, max_x = Xs[0], Xs[-1]; dx = max_x - min_x
	min_y, max_y = min(Ys), max(Ys); dy = max_y - min_y	
	plt.arrow(0 - dx, 0, 2 * dx, 0)
	plt.arrow(0, 0 - dy, 0, 2 * dy)

	for x, y in Df:
		plt.scatter(x, y, s=1)

	plt.show()

	'''
	xf = []
	yf = []
	for i in spectrum(start, end, d):
		if i not in exceptions:
			xf.append(i)
			yf.append(func(i))

	min_x, max_x = xf[0], xf[-1]; av_x = (min_x + max_x) / 2; dx = max_x - min_x
	min_y, max_y = min(yf), max(yf); av_y = (min_y + max_y) / 2; dy = max_y - min_y
	plt.scatter(xf, yf, s=1, c="red")
	plt.arrow(0 - dx, 0, 2 * dx, 0)
	plt.arrow(0, 0 - dy, 0, 2 * dy)
	plt.show()
	'''
