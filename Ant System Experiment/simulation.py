from dp_tsp import dp_tsp
from dp_tsp import generate_distances
from as_tsp import ant_system


def main():
	min_cost_limit = 1
	max_cost_limit = 10
	num_of_runs = 1

	simulation_parameters = [
		#alpha, beta, rho
		(2.0, 5.0, 1),
		(2.0, 5.0, 0.5),
		(2.0, 10, 1),
		(2.0, 10, 0.5),
		(1.0, 5.0, 1),
		(1.0, 5.0, 0.5),
		(1.0, 10, 1),
		(1.0, 10, 0.5)
	]
	
	#Graph 1
	num_of_nodes = 9
	distances_1 = generate_distances(num_of_nodes, min_cost_limit, max_cost_limit)
	optimal_solution_1 = dp_tsp(distances_1)
	print(f"Optimal solution for 1: {optimal_solution_1}")
	
	all_solutions_1 = []
	best_solutions_1 = []

	for params in simulation_parameters:
		all_solutions_1_ = []
		for num_run in range(num_of_runs):
			all_solutions_1_.append(ant_system(
				distances_1, 
				1000, 
				50, 
				alpha=params[0], 
				beta=params[1], 
				rho=params[2], 
				Q=20
			))
		all_solutions_1.append(all_solutions_1_)

	print(f"Optimal solution for 1: {optimal_solution_1}")
	print("All solutions for 1")
	print(all_solutions_1)

	#Graph 2
	num_of_nodes = 10
	distances_2 = generate_distances(num_of_nodes, min_cost_limit, max_cost_limit)
	optimal_solution_2 = dp_tsp(distances_2)
	
	all_solutions_2 = []
	best_solutions_2 = []

	for params in simulation_parameters:
		all_solutions_2_ = []
		for num_run in range(num_of_runs):
			all_solutions_2_.append(ant_system(
				distances_2, 
				1000, 
				50, 
				alpha=params[0], 
				beta=params[1], 
				rho=params[2], 
				Q=20
			))
		all_solutions_2.append(all_solutions_2_)

	print(f"Optimal solution for 2: {optimal_solution_2}")
	print("All solutions for 2")
	print(all_solutions_2)


	#Graph 3
	num_of_nodes = 11
	distances_3 = generate_distances(num_of_nodes, min_cost_limit, max_cost_limit)
	optimal_solution_3 = dp_tsp(distances_3)

	all_solutions_3 = []
	best_solutions_3 = []

	for params in simulation_parameters:
		all_solutions_3_ = []
		for num_run in range(num_of_runs):
			all_solutions_3_.append(ant_system(
				distances_3, 
				10, 
				50, 
				alpha=params[0], 
				beta=params[1], 
				rho=params[2], 
				Q=20
			))
		all_solutions_3.append(all_solutions_3_)

	print(f"Optimal solution for 3: {optimal_solution_3}")
	print("All solutions for 3")
	print(all_solutions_3)



if __name__ == "__main__":
	main()