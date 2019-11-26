def same_as_last_iteration(previous_results):
	return previous_results[-1]

def same_as_two_iterations_ago(previous_results):
	return previous_results[-2]

def same_as_five_iterations_ago(previous_results):
	return previous_results[-5]

def rounded_average(previous_results, num_iterations = 4):
	sum_all = sum(previous_results[len(previous_results) - num_iterations : len(previous_results)])
	return int(sum_all / num_iterations)
