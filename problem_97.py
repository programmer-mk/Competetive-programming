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
        
        @cache
        def max_earn(num):
            if num == 0:
                return 0
            elif num == 1:
                return number_points[1]
            else:
                return max(max_earn(num-2) + number_points[num], max_earn(num-1))
        
        return max_earn(max_number)
        
    
        