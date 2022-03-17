class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not len(nums):
            return []
        
        result = [[nums[0]]]
        for num_idx in range(1, len(nums)) :
            perm_count = len(result)
            for perm_idx in range(perm_count):
                for j in range(num_idx+1):
                    current_perm = result[perm_idx].copy()
                    current_perm.insert(j, nums[num_idx])
                    result.append(current_perm)
            
            result = result[perm_count:]
        return result
        