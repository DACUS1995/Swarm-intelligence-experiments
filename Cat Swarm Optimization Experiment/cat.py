import random
import numpy as np
from enum import Enum

from simulation import SMP, SRD

class Behavior(Enum):
	SEEKING = 1
	TRACING = 2


class Cat:
	def __init__(self, behavior, position, velocities, vmax):
		self.behavior = behavior
		self._position = position
		self._velocities = velocities
		self._vmax = vmax
		self._dimension_size = len(self._position)

	def evaluate(self, function):
		pass

	def move(self, function):
		if self._behavior == Behavior.SEEKING:
			candidate_moves = []

			for j in range(SMP):
				candidate_moves.append(
					[
						random.uniform(self._position[
							idx_dim - (idx_dim * SRD) / 100, 
							idx_dim + (idx_dim * SRD) / 100
						]) 
						for idx_dim in range(self._dimension_size)
					]
				)
			
			fitness_values = [function(candidate) for candidate in candidate_moves]

			fit_min = max(fitness_values)
			fit_max = min(fitness_values)

			probabilities = [abs(value - fit_max) / (fit_max - fit_min) for value in fitness_values]

			next_position_idx = np.random.choice(SMP, 1, p=probabilities)[0]
			self._position = candidate_moves[next_position_idx]
		elif self._behavior == Behavior.TRACING:
			pass
		else:
			raise Exception("Unreachable")