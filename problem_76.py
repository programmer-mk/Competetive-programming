def find_corrupt_numbers(nums):
  N = len(nums)
  if N <= 0:
      return [-1, -1]

  nums.sort()
  result = []
  for idx, num in enumerate(nums):
    if idx == 0 and num != 1:
      result.append(1)
    elif idx > 0 and nums[idx] == nums[idx-1]:
      result.append(nums[idx])
    elif idx > 0 and nums[idx] > nums[idx-1] + 1:
      result.append(nums[idx-1]+1)
    elif idx == N-1 and num != N:
      result.append(N)
    else:
      print('number: '+ str(num) + ' is fine.')

  return result
