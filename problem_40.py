def max_sub_array_of_size_k(k, arr):
  current_sum, max_sum  = 0.0, 0.0
  start_window = 0
  N = len(arr)
  for end_window in range(N):
    current_sum += arr[end_window]
 
    if end_window >= k - 1:
      if current_sum > max_sum:
        max_sum = current_sum

      current_sum -= arr[start_window]
      start_window += 1
    
  return max_sum

      
    

