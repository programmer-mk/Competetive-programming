class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        
        left = 0
        right = N-1
        while left < right:
            mid = (left+right) // 2
            if nums[mid] >= nums[right]:
                left=mid+1
            else:
                right = mid
                
        return nums[left]
        