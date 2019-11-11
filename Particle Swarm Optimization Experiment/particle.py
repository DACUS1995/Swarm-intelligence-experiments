import random
import sys

class Particle:
	def __init__(self, param_pair, starting_position = None, num_dimensions = 2):
		self.position = []          # particle position
		self.velocity = []          # particle velocity
		self.pos_best = []          # best position individual
		self.err_best = sys.maxsize # best error individual
		self.err = sys.maxsize      # error individual
		self.param_pair = param_pair
		self.num_dimensions = num_dimensions

		for i in range(0, num_dimensions):
			self.velocity.append(random.uniform(-1,1))
			if starting_position != None:
				self.position.append(starting_position[i])
			else:
				self.position.append(random.uniform(-5, 5))


	def evaluate(self, cost_fn):
		self.err = cost_fn(self.position)

		# Update best score for the particle
		if self.err < self.err_best or self.err_best == -1:
			self.pos_best = self.position.copy()
			self.err_best = self.err


	def update_velocity(self, pos_best_g, pso_variant):
		w = 1       # constant inertia weight (how much to weigh the previous velocity)
		c1 = self.param_pair[0]        # cognative constant
		c2 = self.param_pair[1]        # social constant
		chi = 1
	
		if pso_variant == "vanilla":
			pass
		elif pso_variant == "inertia_weight":
			w = 0.7
		elif pso_variant == "constriction_factor":
			chi = 0.729

		
		for i in range(0, self.num_dimensions):
			r1 = random.random()
			r2 = random.random()
			
			vel_cognitive = c1 * r1 * (self.pos_best[i] - self.position[i])
			vel_social = c2 * r2 * (pos_best_g[i] - self.position[i])
			self.velocity[i] = chi * (w * self.velocity[i] + vel_cognitive + vel_social)


	# update the particle position based off new velocity updates
	def update_position(self, bounds):
		for i in range(0, self.num_dimensions):
			self.position[i] = self.position[i] + self.velocity[i]
			
			# adjust maximum position if necessary
			if self.position[i] > bounds[1]:
				self.position[i] = bounds[1]

			# adjust minimum position if neseccary
			if self.position[i] < bounds[0]:
				self.position[i] = bounds[0]