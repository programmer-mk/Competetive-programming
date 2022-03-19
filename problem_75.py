class Solution:
    
    def search_pairs(self, start_idx,  nums, first, second, target, result):
        end_idx = len(nums) - 1
        while(start_idx < end_idx):
            #print(f'start index: {start_idx}, end index : {end_idx}')
            temp_sum = nums[start_idx] + nums[end_idx] + first + second
            if temp_sum == target:
                result.append([first, second, nums[start_idx], nums[end_idx]])
                start_idx += 1
                while(start_idx < len(nums) and nums[start_idx] == nums[start_idx-1]):
                    start_idx += 1
            elif temp_sum < target:
                start_idx += 1
            else:
                end_idx = end_idx - 1
                    
            
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        if N < 4:
            return []
        result = []
        nums.sort()

        for i in range(N-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, N-2):
                if j-1 > i and nums[j] == nums[j-1]:
                    continue
                self.search_pairs(j+1, nums, nums[i], nums[j], target, result)
                
        return result
                