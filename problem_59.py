"""
    Iterative solutions(BFS)
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        if not len(nums):
            return result
        result.append([])
        for current_number in nums:
            current_size = len(result)
            for i in range(current_size):
                current_set = result[i].copy()
                current_set.append(current_number)
                result.append(current_set)
            
        return result