class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        full_xor = 0
        for num in nums:
            full_xor ^= num
           
        diff_bit_position = 0
        while not (full_xor & 1):
            diff_bit_position += 1
            full_xor = full_xor // 2
                
        num1 = 0
        num2 = 0
        for num in nums:
            bit = (num >> diff_bit_position) & 1
            if bit == 1:
                num1 ^= num
            else:
                num2 ^= num
                # bit = 0
                
        return [num1, num2]