class Solution:
    """
        One huge test case exceeds runtime limit
    """
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        if k == 0:
            return 0
        
        result = []
        curr_product = 1
        N = len(nums)
        start_window = 0
        for end_window in range(N):
            curr_product *= nums[end_window]
            while curr_product >= k and start_window < N:
                curr_product /= int(nums[start_window])
                start_window += 1
           
            temp_list = []
            for idx in range(end_window, start_window - 1, -1):
                temp_list.append(nums[idx])
                result.append(temp_list)
                
        return len(result)