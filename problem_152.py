class Solution:
    """
        input: [7,1,5,3,6,4]
        min_left = [7, 1, 1, 1, 1, 1]
        max_right = [7, 6, 6, 6, 6, 4]
    
        Complexity:
         - time: O(2N)
         - space: O(2N)
    """
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        max_right = [-1] * N
        min_left = [-1] * N
        min_val = math.inf
        max_val = -math.inf
        for i in range(N):
            current_min = min(min_val, prices[i])
            min_left[i] = current_min
            min_val = current_min
            
        for i in range(N-1, -1, -1):
            current_max = max(max_val, prices[i])
            max_right[i] = current_max
            max_val = current_max

        max_profit = 0
        for i in range(N):
            max_profit = max(max_profit, max_right[i]-min_left[i])
            
        return max_profit
    
    