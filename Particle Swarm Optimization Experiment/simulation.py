from pso import PSO
import cost_functions
import pandas as pd
import numpy as np

import sys


NUM_ITERATIONS = 500
NUM_POPULATION = 50

def  print_experiment_settings(function, pso_variant, topology, param_pair):
	print(f"Function used: {function} function")
	print(f"PSO variant: {pso_variant}")
	print(f"Topology: {topology}")
	print(f"Parameter used: {param_pair} \n")


def run_experiment(
		function_name, 
		topology, 
		param_pair, 
		pso_variant, 
		num_particles=NUM_POPULATION,
		num_inter=NUM_ITERATIONS
	):
		print("------------START EXPERIMENT-------------")
		print_experiment_settings(function_name, pso_variant, topology, param_pair)

		function = getattr(cost_functions, f"{function_name}_fn")

		err_best_all = sys.maxsize
		pos_best_all = None

		for i in range(10):
			err_best, pos_best = PSO.run(
				function,
				(-5.12, 5.12),
				pso_variant,
				num_particles,
				num_inter,
				topology,
				param_pair
			)

			if err_best < err_best_all:
				err_best_all = err_best
				pos_best_all = pos_best
			
		err_best_all = format(err_best_all, '.10f')
		pos_best_all = [format(x, '.10f') for x in pos_best_all]

		print(f'Best Position: {pos_best_all}')
		print(f'Best error: {err_best_all}')
		print("-------------END EXPERIMENT--------------\n\n")

		return err_best_all, pos_best_all


def main():
	param_pairs = [
		(1, 0.5),
		(0.5, 1),
		(2.05, 2.05)
	]

	pso_variants = [
		"vanilla",
		"inertia_weight",
		"constriction_factor"
	]

	topologies = [
		"fully_connected",
		"ring",
		"four_n"
	]

	functions = [
		"spherical",
		"rastrigin",
		"griewank",
		"rosenbrock"
	]


	allResults = []

	for function in functions:
		for pso_variant in pso_variants:
			for topology in topologies:
				for param_pair in param_pairs:
					err, pos = run_experiment(
						function, 
						topology, 
						param_pair, 
						pso_variant
					)

					allResults.append(
						[
							function, 
							topology, 
							param_pair, 
							pso_variant,
							err,
							np.array(pos)
						]
					)
				
	data = np.array(allResults)
	dataset = pd.DataFrame({
		'function': data[:, 0], 
		'topology': data[:, 1],
		'param_pair': data[:, 2],
		'pso_variant': data[:, 3],
		'value': data[:, 4],
		'coord': data[:, 5]
	})

	dataset.to_excel("output.xlsx")

	print(dataset)


if __name__ == "__main__":
	main()