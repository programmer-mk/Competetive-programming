class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff_num = 0
        while x > 0 and y > 0:
            if x % 2 != y % 2:
                diff_num = diff_num + 1
            x = int(x / 2)
            y = int(y / 2)

        while x > 0:
            if x % 2:
                diff_num = diff_num + 1
            x = int(x / 2)

        while y > 0:
            if y % 2:
                diff_num = diff_num + 1
            y = int(y / 2)

        return diff_num