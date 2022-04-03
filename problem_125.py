class Solution:
    
    def rob_recusive(self, nums: List[int], index, sum, dp):
        if index >= len(nums):
            return sum
        
        if dp[index] != -1:
            return dp[index]
        
        include = self.rob_recusive(nums, index+2, sum+nums[index], dp.copy())
        exclude = self.rob_recusive(nums, index+1, sum, dp.copy())
        dp[index] = max(include, exclude)
        return dp[index]
        
    
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [-1 for _ in range(N)]
        return self.rob_recusive(nums, 0, 0, dp)
       
        
        