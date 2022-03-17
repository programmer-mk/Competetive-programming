class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        if N == 0:
            return -1
        
        start, end = 0, N-1
        while(start <= end):
            mid = int((start + end) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return start