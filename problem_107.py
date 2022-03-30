import math

def count_subsets_recursive(nums, index, curr_subset, subset_count, S, dp):
  if index >= len(nums):
    return 0

  if dp[index][S] != math.inf:
      return dp[index][S]

  extend_subset = curr_subset.copy()
  extend_subset.append(nums[index])
  inc_count = count_subsets_recursive(nums, index + 1, extend_subset, subset_count, S - nums[index], dp)
  exc_count = count_subsets_recursive(nums, index + 1, curr_subset, subset_count, S, dp)
  
  if  nums[index] == S:
    dp[index][S] =  1 + inc_count + exc_count
  else:
     dp[index][S] =  inc_count + exc_count
    
  return dp[index][S]


def count_subsets(nums, sum):
  dp = [[math.inf for _ in range(sum+1)] for _ in range(len(nums))]
  subset_count = count_subsets_recursive(nums, 0, [], 0, sum, dp)
  return subset_count

def main():
  print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
  print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()

