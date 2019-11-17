import random

from strategies import same_as_last_iteration, rounded_average, same_as_two_iterations_ago, same_as_five_iterations_ago


def print_results(results):
	print("The attendance for each week")
	print(results)

	average = sum(results) / len(results)
	print(f"Average: {average}")

	count = sum(map(lambda x : x < 50, results))
	print(f"The number of weeks with the attendance <= 50: {count}")

	count = sum(map(lambda x : x > 50 and x <= 60, results))
	print(f"The number of weeks with the attendance > 50 and <= 60: {count}")

	count = sum(map(lambda x : x > 70, results))
	print(f"The number of weeks with the attendance > 70: {count}")

	count = sum(map(lambda x : x <= 50, results))
	print(f"The number of weeks with the attendance <= 50: {count}")

def run_simulation(population_size, iterations = 100, strategies = None, previous_results = []):
	if strategies == None:
		raise Exception("No valid strategies were provided for this simulation run.")

	start = len(previous_results)

	for iteration in range(iterations):
		strategy = random.sample(strategies, 1)[0]
		previous_results.append(
			min(strategy(previous_results), 100)
		)

	end = len(previous_results)

	print_results(previous_results[start:end])

if __name__ == "__main__":
	population_size = 100
	iterations = 100
	strategies = [same_as_last_iteration, rounded_average, same_as_two_iterations_ago, same_as_five_iterations_ago]
	previous_results = [44, 78, 56, 15, 23, 67, 84, 34, 45, 76, 40, 56, 22 ,35]

	run_simulation(
		population_size,
		iterations,
		strategies,
		previous_results
	)