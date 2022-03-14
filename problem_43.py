class Solution:
    """
        Leetcode time limit exceeded in one test case
    """
    
    def search(self, nums: List[int], start_index, target: int):
        left = start_index
        right = len(nums) - 1
        min_diff = math.inf
        result_sum = math.inf
        while(left < right):
            sum = nums[left] + nums[right]
            
            if abs(target - sum) < min_diff:
                min_diff = abs(target - sum)
                result_sum = sum
                
            if sum < target:
                left += 1
            elif sum == target:
                return sum, 0
            else:
                right -= 1
                
        return result_sum, min_diff
            
            
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        N = len(nums)
        nums.sort()
        result_min_diff = math.inf
        result_sum = math.inf
        for i in range(N-2):
            for j in range(i+1, N-1):
                sum, min_diff = self.search(nums, j, target - nums[i])
                if min_diff == 0:
                    return sum + nums[i]
                if min_diff < result_min_diff:
                    result_sum = sum + nums[i]
                    result_min_diff = min_diff

        return result_sum
        