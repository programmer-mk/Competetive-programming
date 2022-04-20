class Solution:
    
    def combine_helper(self, n: int, count: int, k: int, temp: List[int], result: List[List[int]]):
        if len(temp) == k:
            result.append(temp)
            return
        
        if count > n:
            return
        
        combination = temp
        combination.append(count)
        self.combine_helper(n, count+1, k, combination.copy(), result)
        combination.remove(count)
        self.combine_helper(n, count+1, k, combination.copy(), result)
            
        
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.combine_helper(n, 1, k, [], result)
        return result
    
