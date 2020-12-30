def max_window_sum(arr,w_size):
	if len(arr) < w_size:
		return None
	running_sum = run_index = 0
	max_val =  float("-inf")

	for item in range(w_size):
		running_sum += arr[item]

	for item in range (w_size , len(arr)):
		if running_sum > max_val:
			max_val = running_sum
		running_sum -= arr[run_index]
		running_sum += arr[item]
		run_index += 1

	if running_sum > max_val:
		max_val = running_sum
	return max_val

print(max_window_sum([1,2,3,4,5,6],3)) #3
print(max_window_sum([1,32,3,4,5,6],2)) #35

