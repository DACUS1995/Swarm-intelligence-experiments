from particle import Particle
import sys
import random

class PSO:
	@staticmethod
	def run(cost_fn, bounds, pso_variant, num_particles, num_inter, topology, param_pair):
		if topology == "fully_connected":
			return PSO._run_full(cost_fn, bounds, pso_variant, num_particles, num_inter, param_pair)
		elif topology == "ring":
			return PSO._run_ring(cost_fn, bounds, pso_variant, num_particles, num_inter, param_pair)

	@staticmethod
	def _run_full(cost_fn, bounds, pso_variant, num_particles, num_inter, param_pair):
		err_best = -1
		pos_best = []

		swarm = []
	
		for i in range(0, num_particles):
			swarm.append(Particle(
				param_pair=param_pair,
				starting_position=[random.uniform(bounds[0], bounds[1]) for _ in range(len(bounds))],
			))

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

		return err_best, pos_best


	@staticmethod
	def _run_ring(cost_fn, bounds, pso_variant, num_particles, num_inter, param_pair):
		err_best = -1
		pos_best = []

		swarm = []

		for i in range(0, num_particles):
			swarm.append(Particle(
				param_pair=param_pair,
				starting_position=[random.uniform(bounds[0], bounds[1]) for _ in range(len(bounds))],
			))

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

		return err_best, pos_best


def main():
	pass


if __name__ == "__main__":
	pass