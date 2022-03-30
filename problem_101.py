import math

def can_partition_recursive(nums, index, sum1, sum2, dp):
  if index == len(nums):
    return abs(sum1 - sum2)

  if dp[index][sum1] != -1:
    return dp[index][sum1]

  diff = min(can_partition_recursive(nums, index+1, sum1+nums[index], sum2, dp), \
             can_partition_recursive(nums, index+1, sum1, sum2+nums[index], dp) )

  dp[index][sum1] = diff
  return diff
  

def can_partition(nums):
  if len(nums) < 2:
    return -1

  dp = [[-1 for _ in range(sum(nums)+1)] for _ in range(len(nums))]
  return can_partition_recursive(nums, 0, 0, 0, dp)


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 9])))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
  print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
