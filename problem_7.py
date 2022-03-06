class Solution:
    def reverse(self, x: int) -> int:
        result_str = ""
        if x == 0:
            return 0
        elif x < 0:
            positive = False
        else:
            positive = True

        num_str = str(abs(x))
        skip_zeroes = True
        for index in range(len(num_str)-1, -1, -1):
            if num_str[index] != 0:
                result_str += num_str[index]
                if skip_zeroes:
                    skip_zeroes = False
            elif not skip_zeroes:
                result_str += num_str[index]

        if positive:
            result_num = int(result_str)
        else:
            result_num = int(result_str) * - 1

        max_int = 2**31 - 1
        if result_num > max_int or result_num < -1 * max_int:
            return 0
        else:
            return result_num
