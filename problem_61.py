class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        result.append([])
        nums.sort()
        latest_subsets = []
        for num_idx in range(len(nums)):
            if num_idx > 0 and nums[num_idx] == nums[num_idx-1]:
                subsets_count = len(latest_subsets)
                current_subsets = latest_subsets
            else:
                subsets_count = len(result)
                current_subsets = result
            
            new_subsets = []
            for subs_idx in range(subsets_count):
                new_subset = current_subsets[subs_idx].copy()
                new_subset.append(nums[num_idx])
                new_subsets.append(new_subset)
                current_subsets.append(new_subset)
            
            latest_subsets = new_subsets
            if num_idx > 0 and nums[num_idx] == nums[num_idx-1]:
                result = result + new_subsets
             
        return result
        