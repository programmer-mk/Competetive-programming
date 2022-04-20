class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        temp_list = [[]]
        count = 1
        while temp_list and count <= n:
            size = len(temp_list)
            for i in range(size):
                combination = temp_list[i].copy()
                combination.append(count)
                temp_list.append(combination)
                if len(combination) == k:
                    result.append(combination.copy())
            count += 1
        
        return result
    
