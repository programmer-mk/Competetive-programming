class Solution:

    def occurencies(self, word):
        n = len(word)
        result = ""
        current_count = 0

        for index in range(n):
            if index > 0 and word[index] != word[index-1]:
                result += f"{current_count}{word[index-1]}"
                current_count = 1
                if index == n-1:
                    result += f"{current_count}{word[index]}"
            else:
                current_count += 1
                if index == n-1:
                    result += f"{current_count}{word[index]}"

        return result


    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            word = self.countAndSay(n-1)
            occurencies = self.occurencies(word)
            print(f'for: {n}  say: {word} with {occurencies}')
            return occurencies
