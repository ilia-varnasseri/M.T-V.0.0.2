import math
def parse(n):
	def isprime(x):

		if x == 1:
			return False

		for i in range(2, x):
			if x % i == 0:
				return False
		
		else:
			return True

	def prime(x):
		i = 0
		c = 0
		while i != x:
			c += 1

			if isprime(c):
				i += 1

		return c

	def calc(elems):
		prod = 1
		for num, power in elems:
			prod *= num ** power

		return prod

	elems = []
	current_prime_index = 1
	ess_n = n

	while n != 1:
		i = 0
		current_prime = prime(current_prime_index)

		while n % current_prime == 0:
			i += 1
			n /= current_prime

		if i != 0:	
			elems.append((current_prime, i))

		current_prime_index += 1

	return dict(elems)



def gcd(numbers):
	nums = [parse(num) for num in numbers]
	x = []

	def calc(elems):
		prod = 1
		for num, power in elems:
			prod *= num ** power

		return prod

	for number in nums:

		for n, power in number.items():

			if all([n in i.keys() for i in nums]):

				if n not in dict(x).keys():
					x.append((n, min([p[n] for p in nums])))

	return calc(x)


def lcd(m, n):
	return abs(m * n) // gcd(m, n)

