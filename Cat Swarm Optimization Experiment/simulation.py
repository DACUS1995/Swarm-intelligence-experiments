import numpy as np
import sys

import cost_functions
import cso


NUM_RUNS = 30
NUM_CATS = 50
MR = 2 #percentage
SMP = 5 #seeking memory pool
SRD = 20 #percentage - seeking range of the selected dimension
c1 = 2
num_dimensions = 2
v_max = 1

def run_experiment(function_name, num_iteration):
	function = getattr(cost_functions, f"{function_name}_fn")

	results = []
	results_pos = []
	avg = 0

	for _ in range(NUM_RUNS):
		best, best_pos = cso.CSO.run(
			num_iteration, 
			function, 
			num_cats=NUM_CATS, 
			MR=MR, 
			num_dimensions=num_dimensions, 
			v_max=v_max
		)

		results_pos.append(best_pos)
		results.append(best)
	
	best_all = min(results)
	best_all_pos = results_pos[results.index(best_all)]

	return best_all, best_all_pos, (sum(results) / len(results))


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
			best, best_pos, avg = run_experiment(function, num_iteration)
			print(f"Function={function}, Iterations={num_iteration} | best={format(best, '.10f')}, best_pos={best_pos}, avg={format(avg, '.10f')}")


if __name__ == "__main__":
	main()