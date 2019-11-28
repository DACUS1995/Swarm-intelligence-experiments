import numpy as np
import sys

import cost_functions
from cso import CSO


NUM_RUNS = 30
NUM_CATS = 50
MR = 2 #percentage

def run_experiment(function_name, num_iteration):
	function = getattr(cost_functions, f"{function_name}_fn")

	results = []
	avg = 0

	for _ in range(NUM_RUNS):
		results.append(CSO.run(num_iteration, function, num_cats=NUM_CATS, MR=MR))

	return min(results), (float)(results / len(results))


def main():
	functions = [
		"spherical",
		"rastrigin",
		"griewank",
		"rosenbrock"
	]

	max_iterations = [50, 100, 500]

	for function in functions:
		for num_iteration in max_iterations:
			best, avg = run_experiment(function, num_iteration)


if __name__ == "__main__":
	main()