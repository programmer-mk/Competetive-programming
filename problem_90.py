class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        result_num = 0
        base = 0
        while n > 0:
            bit = n % 2
            if bit == 0:
                result_num += 2**base
            n = n // 2    
            base += 1   
        return result_num
        