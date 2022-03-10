class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = int(n * (n+1) / 2)
        collected_sum = 0
        for num in nums:
            collected_sum += num

        return expected_sum - collected_sum