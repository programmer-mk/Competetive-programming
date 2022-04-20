class Solution:
    
    def check_character(self, character, word):
        if character != '#':
            word.append(character)
        else:
            if len(word):
                word.pop()
            
    """
        Complexity:
            - Space O(m+n)
            - Time O(2*(m+n))
    """
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_clear = []
        t_clear = []
        index = 0
        
        while index < len(s) and index < len(t):
            self.check_character(s[index], s_clear)
            self.check_character(t[index], t_clear)
            index += 1
            
        while index < len(s):
            self.check_character(s[index], s_clear)
            index += 1
        
        while index < len(t):
            self.check_character(t[index], t_clear)
            index += 1
            
        if len(s_clear) != len(t_clear):
            return False
        index = 0
        while index < len(s_clear):
            if t_clear[index] != s_clear[index]:
                return False
            index += 1
        return True
            
        
            
        