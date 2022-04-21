class Solution:
    
    def merge(self, nums, start, mid, end):
        temp = [0] * (end-start + 1)
        i, j, k = start, mid+1, 0
        while i <= mid and j <= end:
            if nums[i] <= nums[j]:
                temp[k] = nums[i]
                i += 1
            else:
                temp[k] = nums[j]
                j += 1
            k+= 1
            
        while i <= mid:
            temp[k] = nums[i]
            k += 1
            i += 1
            
        while j <= end:
            temp[k] = nums[j]
            k += 1
            j += 1
        
        for i in range(start, end+1):
            nums[i] = temp[i - start]
            
    
    def merge_sort(self, nums, start, end):
        if start < end:
            mid = (start + end) // 2
            self.merge_sort(nums, start, mid)
            self.merge_sort(nums, mid+1, end)
            self.merge(nums, start, mid, end)
    
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums)-1)
        return nums
        