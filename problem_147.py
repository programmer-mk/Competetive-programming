class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        occurencies = {}
        for num in nums:
            occurencies[num] = True
        
        max_count = 0
        for num in nums:
            count = 1
            temp_num = num - 1
            while occurencies.get(temp_num):
                del occurencies[temp_num]
                temp_num -= 1
                count += 1
                
            temp_num = num + 1
            while occurencies.get(temp_num):
                del occurencies[temp_num]
                temp_num += 1
                count += 1
                
            max_count = max(max_count, count)
            
        return max_count
                
            
        