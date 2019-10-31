import random

class Particle:
	def __init__(self):
		self.position = []          # particle position
		self.velocity = []          # particle velocity
		self.pos_best = []          # best position individual
		self.err_best = -1          # best error individual
		self.err = -1               # error individual

		for i in range(0, num_dimensions):
			self.velocity.append(random.uniform(-1,1))
			self.position.append(x[i])

	def evaluate(self, cost_fn):
		self.err = cost_fn(self.position)

		# Update best score for the particle
		if self.err < self.err_best or self.err_best == -1:
			self.pos_best = self.position_i.copy()
			self.err_best = self.err

	def update_velocity(self, pos_best_g):
		w = 0.5       # constant inertia weight (how much to weigh the previous velocity)
		c1 = 1        # cognative constant
		c2 = 2        # social constant
		
		for i in range(0, num_dimensions):
			r1 = random.random()
			r2 = random.random()
			
			vel_cognitive = c1 * r1 * (self.pos_best[i] - self.position[i])
			vel_social = c2 * r2 * (pos_best_g[i] - self.position[i])
			self.velocity[i] = w * self.velocity[i] + vel_cognitive + vel_social

	# update the particle position based off new velocity updates
	def update_position(self, bounds):
		for i in range(0, num_dimensions):
			self.position[i] = self.position[i] + self.velocity[i]
			
			# adjust maximum position if necessary
			if self.position[i] > bounds[i][1]:
				self.position[i] = bounds[i][1]

			# adjust minimum position if neseccary
			if self.position[i] < bounds[i][0]:
				self.position[i] = bounds[i][0]