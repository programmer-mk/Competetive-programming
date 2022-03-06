class Solution:
    def firstUniqChar(self, s: str) -> int:
        occurencies = {}
        for character in s:
            count = occurencies.get(character)
            if count is None:
                occurencies[character] = 1
            else:
                occurencies[character] = count + 1

        for index, character in enumerate(s):
            if occurencies.get(character) == 1:
                return index

        return -1