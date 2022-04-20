class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = []
        dp = [-1]*(amount+1)
        
        def count_change_heper(sum, steps):
            if sum > amount:
                return math.inf
            if sum == amount:
                return 0
            if dp[sum] != -1:
                return dp[sum]
            
            min_steps = math.inf
            for coin in coins:
                curr_steps = 1+count_change_heper(sum+coin, steps)
                if curr_steps < min_steps:
                    min_steps = curr_steps
            dp[sum] = min_steps
            return min_steps
                
        if amount == 0:
            return 0
        steps = count_change_heper(0, 0)
        if steps == math.inf:
            return -1
        else:
            return steps