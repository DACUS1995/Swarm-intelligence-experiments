import random
from enum import Enum

class Behavior(Enum):
	SEEKING = 1
	TRACING = 2


class Cat:
	def __init__(self, behavior, position, velocities, vmax):
		self.behavior = behavior
		self._position = position
		self._velocities = velocities
		self._vmax = vmax

	def evaluate(self, function):
		pass

	def move(self):
		if self._behavior == Behavior.SEEKING:
			pass
		elif self._behavior == Behavior.TRACING:
			pass
		else:
			raise Exception("Unreachable")