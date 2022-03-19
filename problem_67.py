class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = ['']
        for character in s:
            N = len(result)
            new_list_size = 0
            for i in range(N):
                temp_str = result[i]
                if character.isdigit():
                    result.append(temp_str + character)
                    new_list_size += 1
                else:
                    extended_upper = temp_str + character.upper()
                    extended_lower = temp_str + character.lower()
                    result.append(extended_upper)
                    result.append(extended_lower)
                    new_list_size += 2
            
            result = result[-new_list_size:]  
        
        return result
        