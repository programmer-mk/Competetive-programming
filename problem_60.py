class Solution:
    
    def search(self, nums: List[int], index,  result: List[int]):
        if index < len(nums):
            N = len(result)
            for i in range(N):
                new_list = result[i].copy()
                new_list.append(nums[index])
                result.append(new_list)
            self.search(nums, index + 1, result)
            
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # do this recursively
        result = [[]]
        if not len(nums):
            return result
        self.search(nums, 0, result)
        return result