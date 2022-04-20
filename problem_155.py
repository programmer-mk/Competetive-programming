class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        num_letter = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        
        result = [""]
        for digit in digits:
            cur_size = len(result)
            for index in range(cur_size):
                letters = num_letter.get(int(digit))
                for letter in letters:
                    combination = result[index] + letter
                    result.append(combination)
            result = result[cur_size:]
        return result
            
            