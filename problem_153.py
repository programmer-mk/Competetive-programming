class Solution:
    
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [-1] * N
        
        def rob_helper(index, sum):
            if index >= N:
                return sum
            
            if dp[index] != -1:
                return dp[index]
            
            include = rob_helper(index+2, sum)
            exclude = rob_helper(index+1, sum)
            dp[index] = max(include+nums[index], exclude)
            return dp[index]
            
        return rob_helper(0, 0)
            
        