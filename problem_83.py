class Solution:
    
    def can_partition_recursive(self, nums:List[int], sum, index, dp):
        if index >= len(nums):
            return False
        
        if sum == nums[index]:
            return True
        
        if dp[index][sum] != -1:
            return dp[index][sum] == 1
            
        
        include = False
        if nums[index] < sum:
            include = self.can_partition_recursive(nums, sum - nums[index], index + 1, dp)
            
        exists = include or self.can_partition_recursive(nums, sum, index + 1, dp)
        if exists:
            dp[index][sum] = 1
        else:
            dp[index][sum] = 0
        return exists
    
    def canPartition(self, nums: List[int]) -> bool:
        if not len(nums):
            return False
        
        if sum(nums) % 2 != 0:
            return False
        
        dp = [[-1 for i in range(sum(nums)// 2 + 1)] for j in range(len(nums))]
        #print(dp)
        return self.can_partition_recursive(nums, sum(nums) // 2, 0, dp)
        