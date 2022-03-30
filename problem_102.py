def can_partition(nums):
  if len(nums) < 2:
    return -1

  dp = [[False for _ in range(sum(nums) // 2 + 1)] for _ in range(len(nums))]
  N = len(nums)
  M = sum(nums) // 2 + 1
  for i in range(N):
    dp[i][0] = True

  for i in range(M):
    dp[0][i] = nums[0] == i

  for i in range(1, N):
    for j in range(1, M):
      if dp[i - 1][j]:
        dp[i][j] = dp[i - 1][j]
      elif j >= nums[i]:
        # else include the number and see if we can find a subset to get the remaining sum
        dp[i][j] = dp[i - 1][j - nums[i]]

  sum1 = 0
  # find the largest index in the last row which is true
  for i in range(M-1, -1, -1):
    if dp[N - 1][i]:
      sum1 = i
      break

  sum2 = sum(nums) - sum1
  return abs(sum2 - sum1)


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 9])))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
  print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
