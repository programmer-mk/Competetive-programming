# def solve_knapsack(profits, weights, capacity):
#   # TODO: Write your code here
#   return -1

def solve_snapsack_recursive(profits, index, weights, capacity, dp):
  if index >= len(profits):
    return 0

  if dp[index][capacity] != -1:
    return dp[index][capacity]

  include_profit = 0
  exclude_profit = 0
  if weights[index] <= capacity:
    include_profit = profits[index] + \
      solve_snapsack_recursive(profits, index+1, weights, capacity-weights[index], dp)

  exclude_profit = solve_snapsack_recursive(profits, index+1, weights, capacity, dp)
  dp[index][capacity] = max(include_profit, exclude_profit)
  return max(include_profit, exclude_profit)

def solve_knapsack(profits, weights, capacity):
  dp = [[-1 for i in range(capacity+1)] for j in range(len(profits))]
  return solve_snapsack_recursive(profits, 0, weights, capacity, dp)


def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()

