class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        while(n > 0):
            if n % 2 == 1:
                counter = counter + 1
            n = int(n / 2)

        return counter