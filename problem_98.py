from collections import defaultdict

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        number_points = defaultdict(int)
        max_number = 0
        for num in nums:
            if number_points.get(num):
                number_points[num] += num
            else:
                number_points[num] = num
            max_number = max(max_number, num)
        
        dp = [0] * (max_number+1)
        dp[1] = number_points[1]
        for idx in range(2, max_number+1):
            dp[idx] = max(dp[idx-1], dp[idx-2]+ number_points[idx])
        
        return dp[max_number]