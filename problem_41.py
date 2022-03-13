import math

def smallest_subarray_with_given_sum(s, arr):
  N = len(arr)
  if not N:
    return 0

  subarr_length = math.inf
  start_window = 0
  current_sum = 0

  for end_window in range(N):
    current_sum += arr[end_window]

    while current_sum >= s:
      subarr_length = min(subarr_length, end_window - start_window + 1)
      current_sum -= arr[start_window]
      start_window += 1
  if subarr_length == math.inf:
    return 0
   
  return subarr_length
