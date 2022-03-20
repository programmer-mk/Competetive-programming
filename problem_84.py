
def can_partition_recursive(nums, sum, index):
  if index >= len(nums):
    return False
  if nums[index] == sum:
    return True
  include, exclude = False, False
  if nums[index] < sum:
    include = can_partition_recursive(nums, sum - nums[index], index + 1)
  exclude = can_partition_recursive(nums, sum, index + 1)
  return include or exclude

  
def can_partition(nums, sum):
  if not len(nums):
    return False

  return can_partition_recursive(nums, sum, 0)


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
  print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()

