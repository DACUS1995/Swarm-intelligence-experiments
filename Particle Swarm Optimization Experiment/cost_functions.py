def spherical_fn(x):
	total = 0

	for i in range(len(x)):
		total += x[i]**2
	return total

def rastrigin_fn(x):
	total = 0

	for i in range(len(x)):
		total += x[i]**2
	return total

def griewank_fn(x):
	total = 0

	for i in range(len(x)):
		total += x[i]**2
	return total

def rosenbrock_fn(x):
	total = 0

	for i in range(len(x)):
		total += x[i]**2
	return total