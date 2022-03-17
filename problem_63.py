class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        if not  N:
            return -1
        
        left, right = 0, N-1
        while(left <= right):
            mid = int((left + right)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = right-1
            else:
                # smaller than target
                left = mid+1
                
        return -1
        