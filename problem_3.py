class Solution:
    """
        Memory O(N)
        Time O(2N)
    """
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        result_list = [0] * n
        print(f"input list length: {n}")
        for index, num in enumerate(nums):
            if (k + index >= n):
                temp_index = (k + index) - n
                print(f"temp index: {temp_index}, pushing from front")
            else:
                temp_index = (k + index)
                print(f"temp index: {temp_index}")
            result_list[temp_index] = num

        for index,num in enumerate(result_list):
            nums[index] = result_list[index]


    """
        Memory O(1)
        Time O(N)
    """
    @staticmethod
    def reverse(nums: List[int]):
        n = len(nums)
        mid = int(n / 2)
        for index, num in enumerate(nums[:mid]):
            temp = nums[index]
            nums[index] = nums[n-1-index]
            nums[n-1-index] = temp
        return nums

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums = self.reverse(nums)
        nums[:k] = self.reverse(nums[:k])
        nums[k:] = self.reverse(nums[k:])


    