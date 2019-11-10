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
		elif topology == "four_n":
			return PSO._run_four(cost_fn, bounds, pso_variant, num_particles, num_inter, param_pair)
		else:
			raise Exception(f"Sanity check for topology {topology}")

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
				swarm[j].update_velocity(pos_best, pso_variant)
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
			
			# cycle through swarm and update velocities and position
			for j in range(0, num_particles):
				# determine if current particle is the best from its 2 neighbours
				start = -2
				end = 0

				err_best_locally = -1
				pos_best_locally = []

				for l in range(start, end + 1):
					pos = j + l

					if swarm[pos].err < err_best_locally or err_best_locally == -1:
						err_best_locally = float(swarm[pos].err)
						pos_best_locally = list(swarm[pos].position)

				swarm[j].update_velocity(pos_best_locally, pso_variant)
				swarm[j].update_position(bounds)

				if swarm[j].err < err_best or err_best == -1:
					pos_best = list(swarm[j].position)
					err_best = float(swarm[j].err)


		return err_best, pos_best


	@staticmethod
	def _run_four(cost_fn, bounds, pso_variant, num_particles, num_inter, param_pair):
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
			
			# cycle through swarm and update velocities and position
			for j in range(0, num_particles):
				# determine if current particle is the best from its 4 neighbours
				start = -4
				end = 0

				err_best_locally = -1
				pos_best_locally = []

				for l in range(start, end + 1):
					pos = j + l

					if swarm[pos].err < err_best_locally or err_best_locally == -1:
						err_best_locally = float(swarm[pos].err)
						pos_best_locally = list(swarm[j].position)

				swarm[j].update_velocity(pos_best_locally, pso_variant)
				swarm[j].update_position(bounds)

				if swarm[j].err < err_best or err_best == -1:
					pos_best = list(swarm[j].position)
					err_best = float(swarm[j].err)


		return err_best, pos_best


def main():
	pass


if __name__ == "__main__":
	pass