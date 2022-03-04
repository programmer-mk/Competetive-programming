class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        existing_nums = {}
        for index, num in enumerate(nums):
            existing_index = existing_nums.get(target - num)
            if existing_index is not None:
                return [existing_index, index]
            else:
                existing_nums[num] = index

        #unhappy path
        return []