from cost_functions import sphere_fn
from particle import Particle

class PSO:
	@staticmethod
	def run(self, cost_fn, bounds, pso_variant, num_particles, num_inter):
		err_best = 0
		pos_best = []

		swarm=[]

		for i in range(0, num_particles):
			swarm.append(Particle())

		# Optimization
		for i in range(num_inter):
			# cycle through particles in swarm and evaluate fitness
			for j in range(0, num_particles):
				swarm[j].evaluate(cost_fn)

				# determine if current particle is the best (globally)
				if swarm[j].err < err_best or err_best == -1:
					pos_best = list(swarm[j].position)
					err_best = float(swarm[j].err)
			
			# cycle through swarm and update velocities and position
			for j in range(0, num_particles):
				swarm[j].update_velocity(pos_best)
				swarm[j].update_position(bounds)

		# print('\n Final results:')
		# print(f'Best Position: {pos_best}')
		# print(f'Best error: {err_best}\n')

		return err_best, pos_best


def main():
	pass


if __name__ == "__main__":
	pass