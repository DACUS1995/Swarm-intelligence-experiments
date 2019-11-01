from pso import PSO
import cost_functions

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
				(500, 500),
				pso_variant,
				num_particles,
				num_inter
			)

			if err_best < err_best_all:
				err_best_all = err_best
				pos_best_all = pos_best

		print(f'Best Position: {err_best_all}')
		print(f'Best error: {pos_best_all}')
		print("-------------END EXPERIMENT--------------\n")

		return err_best_all, pos_best_all


def main():
	param_pairs = [
		(1, 1),
		(1, 1),
		(1, 1)
	]

	pso_variants = [
		"vanilla",
		"inertia_weight",
		"constriction-factor"
	]

	topologies = [
		"fully_connected",
		"ring",
	]

	functions = [
		"spherical",
		"rastrigin",
		"griewank",
		"rosenbrock"
	]


	for function in functions:
		for pso_variant in pso_variants:
			for topology in topologies:
				for param_pair in param_pairs:
					run_experiment(
						function, 
						topology, 
						param_pair, 
						pso_variant
					)
				


if __name__ == "__main__":
	main()