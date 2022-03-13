def longest_substring_with_k_distinct(str1, k):
  # TODO: Write your code here
  curr_distinct = {}
  start_window = 0
  max_len = 0
  N = len(str1)
  if k >= N:
    return N

  for end_window in range(N):
    right_char = str1[end_window]
    if right_char not in curr_distinct:
      curr_distinct[right_char] = 1
    else:
      curr_distinct[right_char] += 1

    if len(curr_distinct) > k:
      while(len(curr_distinct) > k):
        left_char = str1[start_window]
        curr_distinct[left_char] -= 1
        if curr_distinct[left_char] == 0:
          del curr_distinct[left_char]
        start_window += 1

    max_len = max(max_len, end_window - start_window + 1)

  return max_len

