class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_occur = [0] * 256
        t_occur = [0] * 256
        for character in s:
            s_occur[ord(character) - ord('a')] = s_occur[ord(character) - ord('a')] + 1
        for character in t:
            t_occur[ord(character) - ord('a')] = t_occur[ord(character) - ord('a')] + 1
        for index in range(0,256):
            if s_occur[index] != t_occur[index]:
                return False
        return True