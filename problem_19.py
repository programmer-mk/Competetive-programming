class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        j = n-1
        while i < j:
            if s[i].lower() == s[j].lower():
                i = i + 1
                j = j - 1
            elif not s[i].isalnum():
                i = i + 1
            elif not s[j].isalnum():
                j = j - 1
            else:
                return False

        return True