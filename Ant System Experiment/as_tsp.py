import numpy as np
from random import randrange
import random

class Ant():
	def __init__(self, position, distances, pheromon_map, alpha, beta, Q):
		self.starting_position = position
		self.position = position
		self.distances = distances
		self.pheromon_map = pheromon_map
		self.path = []
		self.unvisited = [i for i in range(distances.shape[0])]
		self.unvisited.remove(self.position)
		self.path.append(self.position)

		self.total_cost = 0
		self.pheromone_delta = []

		self.alpha = alpha
		self.beta = beta
		self.Q = Q

	def step(self):
		#compute probabilities
		denominator = 0
		for i in self.unvisited:
			denominator += self.pheromon_map[self.position][i] ** self.alpha * (1/self.distances[self.position][i]) ** self.beta

		probabilities = np.zeros([self.distances.shape[0]])
		
		if denominator != 0:
			for j in self.unvisited:
				nominator = self.pheromon_map[self.position][j] ** self.alpha * (1/self.distances[self.position][j]) ** self.beta
				probabilities[j] = nominator / denominator

		# make transition
		destination = -1
		rand = random.random()
		for i, probability in enumerate(probabilities):
			rand -= probability
			if rand <= 0:
				destination = i
				break

		if destination == -1:
			destination = random.choice(self.unvisited)

		# print(probabilities)
		# print(destination)
		# print(self.unvisited)
		self.unvisited.remove(destination)
		self.total_cost += self.distances[self.position, destination]
		self.position = destination
		self.path.append(self.position)

	def go_to_starting_position(self):
		self.total_cost += self.distances[self.position, self.starting_position]
		self.path.append(self.starting_position)
		self.position = self.starting_position

	def compute_pheromon_delta(self):
		self.pheromone_delta = [[0 for j in range(self.distances.shape[0])] for i in range(self.distances.shape[0])]

		for x in range(1, len(self.path)):
			i = self.path[x - 1]
			j = self.path[x]
			self.pheromone_delta[i][j] = self.Q / self.total_cost


def ant_system(distances, num_steps, num_ants, alpha=2.0, beta=5.0, rho=1, Q=20):
	print("Begin Ant System")

	num_nodes = distances.shape[0]
	pheromon_map = np.zeros([num_nodes, num_nodes])


	best_result = float("inf")
	best_path = []
	
	for generation in range(num_steps):
		# print(generation)
		ants = []

		#create ants
		for _ in range(num_ants):
			ants.append(Ant(
				# randrange(0, num_nodes)
				0,
				distances,
				pheromon_map,
				alpha,
				beta,
				Q
			))

		for _ in range(num_nodes - 1):
			for ant in ants:
				ant.step()
		
		#compute delta for pheromons
		for ant in ants:
			ant.go_to_starting_position()
			ant.compute_pheromon_delta()

			if ant.total_cost < best_result:
				best_result = ant.total_cost
				best_path = ant.path


		for i, row in enumerate(pheromon_map):
			for j, col in enumerate(row):
				pheromon_map[i][j] *= (1-rho)

				for ant in ants:
					pheromon_map[i][j] += ant.pheromone_delta[i][j]

	print(best_result)
	print(best_path)
	return best_result


def main():
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

	ant_system(distances, num_steps=500, num_ants=100)


if __name__ == "__main__":
	main()