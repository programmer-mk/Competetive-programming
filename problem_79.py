def solve_snapsack_recursive(profits, index, weights, capacity):
  if index >= len(profits):
    return 0

  include_profit = 0
  exclude_profit = 0
  if weights[index] <= capacity:
    include_profit = profits[index] + \
      solve_snapsack_recursive(profits, index+1, weights, capacity-weights[index])

  exclude_profit = solve_snapsack_recursive(profits, index+1, weights, capacity)
  return max(include_profit, exclude_profit)

def solve_knapsack(profits, weights, capacity):
  return solve_snapsack_recursive(profits, 0, weights, capacity)


def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))