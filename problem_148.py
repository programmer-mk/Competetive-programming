class Solution:
    
    """
    Approaches:
        1. sort array and iterate through sorted array if number on index is not equal index + 1 it's part of result array
           time complexity would be O(nlogn), space complexity is O(1)
           
        2. iterate throguh array and if element is not on his right index, switch number with number on his right index
           time complexity would be O(n), space complexity is O(1)
    """
    def find_disappeared_numbers(self, nums):
        result = []
        i = 0
        while i < len(nums):
            correct = nums[i]-1
            if nums[i] != nums[correct] :
                nums[i],nums[correct]= nums[correct] , nums[i]
            else:
                i=i+1
         
        for idx, num in enumerate(nums):
            if num != idx+1:
                result.append(idx+1)
                
        return result
        