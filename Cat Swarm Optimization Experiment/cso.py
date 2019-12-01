import random
import sys

from cat import Cat, Behavior

class CSO:
	def __init__(self):
		pass

	@staticmethod
	def run(num_iterations, function, num_cats, MR, num_dimensions, v_max):
		num_seeking = (int)((MR * num_cats) / 100)
		best = sys.maxsize
		best_pos = None
		cat_population = []
		
		behavior_pattern = CSO.generate_behavior(num_cats, num_seeking)
		for idx in range(num_cats):
			cat_population.append(Cat(
				behavior = behavior_pattern[idx],
				position = [random.uniform(-5, 5) for _ in range(num_dimensions)],
				velocities = [random.uniform(-v_max, v_max) for _ in range(num_dimensions)], 
				vmax = v_max
			))


		for _ in range(num_iterations):
			#evaluate
			for cat in cat_population:
				score, pos = cat.evaluate(function)
				if score < best:
					best = score
					best_pos = pos

			#apply behavior
			for cat in cat_population:
				cat.move(function, best_pos)
			
			#change behavior
			behavior_pattern = CSO.generate_behavior(num_cats, num_seeking)
			for idx, cat in enumerate(cat_population):
				cat.behavior = behavior_pattern[idx]

		return best, best_pos
			
	@staticmethod
	def generate_behavior(num_cats, num_seeking):
		behavior_pattern = [Behavior.TRACING] * num_cats
		for _ in range(num_seeking):
				behavior_pattern[random.randint(0, num_cats-1)] = Behavior.SEEKING
		
		return behavior_pattern