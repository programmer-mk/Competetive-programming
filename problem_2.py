class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        existing_numbers = {}
        for num in nums:
            if existing_numbers.get(num) is not None:
                return True
            else:
                existing_numbers[num] = 1

        #unhappy path
        return False