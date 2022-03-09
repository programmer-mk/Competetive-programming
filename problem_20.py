class Solution:

    def shortest_word(self, strs: List[str]):
        min_length = 201
        min_index = -1
        for index,word in enumerate(strs):
            if len(word) < min_length:
                min_length = len(word)
                min_index = index
        return min_index, min_length

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        start_word_index, start_word_size = self.shortest_word(strs)
        if start_word_size == 0:
            return ""
        start_word = strs[start_word_index]
        for i in range(201):
            for j in range(len(strs)):

                if j == start_word_index:
                    continue

                if i == start_word_size:
                    return start_word

                if len(strs[j]) > i and strs[j][i] != start_word[i]:
                    return start_word[:i]

        return start_word[:i]





