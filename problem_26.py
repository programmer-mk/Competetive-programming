class Solution:
    def reverseBits(self, n: int) -> int:
        stack = []
        result = 0
        for step in range(32):
            stack.append(n % 2)
            n = int(n / 2)

        for step in range(32):
            if len(stack) > 0:
                bit = stack.pop()
                result += bit * 2**step
            else:
                return result

        return result