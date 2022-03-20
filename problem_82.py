class Solution:
    
    def can_partition_recursive(self, nums:List[int], sum, index):
        if index >= len(nums):
            return False
        
        if sum == nums[index]:
            return True
        
        include = False
        if nums[index] < sum:
            include = self.can_partition_recursive(nums, sum - nums[index], index + 1)
            
        return include or self.can_partition_recursive(nums, sum, index + 1)
    
    def canPartition(self, nums: List[int]) -> bool:
        if not len(nums):
            return False
        
        if sum(nums) % 2 != 0:
            return False
        
        return self.can_partition_recursive(nums, sum(nums) // 2, 0)
        