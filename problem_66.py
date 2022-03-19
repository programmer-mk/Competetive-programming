class Solution:
    
    def binary_search(self, nums: List[int], target: int, bound):
        # bound - left or right
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if not bound:
                # looking for left bound
                if nums[mid] == target and (mid == 0 or nums[mid-1] != nums[mid]):
                    return mid
                elif nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            else:
                # looking for right bound
                 if nums[mid] == target and (mid == len(nums) - 1 or nums[mid+1] != nums[mid]):
                    return mid
                 elif nums[mid] <= target:
                    left = mid + 1
                 else:
                    right = mid - 1
                    
        return -1
        
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not len(nums):
            return [-1, -1]
        
        left = self.binary_search(nums,target, False)
        if left == -1:
            return [-1, -1]
        else:
            right = self.binary_search(nums,target, True)
            return [left, right]
        