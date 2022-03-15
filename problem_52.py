def cyclic_sort(nums):
  N = len(nums)
  i = 0
  while(i < N):
    if nums[i] == i+1:
      print(f'skip: {i}')
      i += 1
    else:
      print(f'swap: {i}')
      j = nums[i]-1
      nums[i], nums[j] = nums[j], nums[i]
  return nums


print(cyclic_sort([1, 5, 6, 4, 3, 2]))