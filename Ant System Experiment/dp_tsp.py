import numpy as np
import itertools 
  


def findsubsets(s, n):
	return list(itertools.combinations(s, n))

def generate_distances(num_of_nodes, min_cost_limit, max_cost_limit):
	distances = np.random.random_integers(min_cost_limit, max_cost_limit, (num_of_nodes, num_of_nodes))
	
	for i in range(distances.shape[0]):
		distances[i, i] = 0
	
	return distances

def dp_tsp(distances):
	print("Begin DP")
	num_of_nodes = distances.shape[0]
	subsets_elements = list(range(1, num_of_nodes))

	subset_costs = {}
	subset_costs[(frozenset([0]), 0)] = 0

	for i in range(1, num_of_nodes):
		subset_costs[(frozenset([0, i]), i)] = distances[0, i]

	for subsets_size in range(2, num_of_nodes):
		subsets = findsubsets(subsets_elements, subsets_size)

		for subset in subsets:
			f_subset = frozenset(subset + tuple([0]))

			for j in subset:
				new_subset = tuple(x for x in subset if x != j)
				new_subset = new_subset + tuple([0])
				
				subset_costs[(f_subset, j)] = min([subset_costs[(frozenset(new_subset), i)] + distances[i, j] for i in new_subset if i != 0])

	subsets_elements.append(0)

	min_distance = min([subset_costs[(frozenset(subsets_elements), j)] + distances[j, 0] for j in range(1, num_of_nodes)])
	
	# print(min_distance)
	return min_distance

def main():
	num_of_nodes = 9
	min_cost_limit = 1
	max_cost_limit = 10

	# distances = generate_distances(
	# 	num_of_nodes,
	# 	min_cost_limit,
	# 	max_cost_limit
	# )

	distances = np.array([
		[0,   29,  20,  21,  16,  31,  100, 12,  4,   31,  18],
		[29,  0,   15,  29,  28,  40,  72,  21,  29,  41,  12],
		[20,  15,  0,   15,  14,  25,  81,  9,   23,  27,  13],
		[21,  29,  15,  0,   4,   12,  92,  12,  25,  13,  25],
		[16,  28,  14,  4,   0,   16,  94,  9,   20,  16,  22],
		[31,  40,  25,  12,  16,  0,   95,  24,  36,  3,   37],
		[100, 72,  81,  92,  94,  95,  0,   90,  101, 99,  84],
		[12,  21,  9,  12,  9,   24,  90,  0,   15,  25,  13],
		[4,   29,  23,  25,  20,  36,  101, 15,  0,   35,  18],
		[31,  41,  27,  13,  16,  3,   99,  25,  35,  0,   38],
		[18,  12,  13,  25,  22,  37,  84,  13,  18,  38,  0]
	])

	#optimal = 253

	dp_tsp(distances)
	# solution_tuple, score = dp_tsp(distances)


if __name__ == "__main__":
	main()