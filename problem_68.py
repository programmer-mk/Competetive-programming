class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        oneTime =0
        twoTime =0
        
        for num in nums:
            oneTime = (oneTime^ num) & (~twoTime)
            twoTime = (twoTime ^ num) & (~oneTime)
        
        return oneTime