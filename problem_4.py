class Solution:

    @staticmethod
    def count_occurencies(nums: List[int]) -> dict():
        occurencies = {}
        for num in nums:
            count = occurencies.get(num)
            if count is None:
                occurencies[num] = 1
            else:
                occurencies[num] = count + 1
        return occurencies


    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_val_1 = {}
        dict_val_2 = {}
        result = []
        occurencies1 = self.count_occurencies(nums1)
        occurencies2 = self.count_occurencies(nums2)
        for num in occurencies1.keys():
            if occurencies1.get(num) is not None and  occurencies2.get(num) is not None:
                min_count = min(occurencies1[num], occurencies2[num])
                for cnt in range(0, min_count):
                    result.append(num)

        return result