class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """

        left_bound_index = 0
        for index, num in enumerate(nums):
            if num != 0 and left_bound_index != index:
                nums[left_bound_index] = num
                left_bound_index = left_bound_index + 1
                nums[index] = 0
            elif num != 0:
                left_bound_index = left_bound_index + 1