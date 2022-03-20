def solve_knapsack(profits, weights, capacity):
  N = len(profits)
  dp = [[0 for i in range(capacity+1)] for j in range(N)]
  for i in range(N):
    dp[i][0] = 0

  for i in range(capacity+1):
    if weights[0] <= i:
      dp[0][i] = profits[0]

  for i in range(1, N):
    for j in range(1, capacity+1):
      include, exclude = 0, 0
      exclude = dp[i-1][j]
      if weights[i] <= j:
        include = profits[i] + dp[i-1][j-weights[i]]
      dp[i][j] = max(exclude, include)

  return dp[N-1][capacity]

def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()