def find_duplicate(nums):
  N = len(nums)
  i = 0
  while(i < N):
    j = nums[i] - 1
    if nums[i] != i + 1:
      if nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]
      else:
        return nums[i]
    else:
      i += 1
  return -1
