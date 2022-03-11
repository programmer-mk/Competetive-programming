class Solution:

    def create_triplet_string(self, nums):
        nums.sort()
        return ' '.join([str(num) for num in nums])

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        founded_triplets = {}
        result = []
        n = len(nums)
        for i in range(0, n-1):
            pairs = {}
            for j in range(i + 1, n):
                if pairs.get(-1*(nums[j] + nums[i])):
                    triplet = [nums[i], -(nums[i] + nums[j]), nums[j]]
                    if founded_triplets.get(self.create_triplet_string(triplet)):
                        continue
                    else:
                        result.append(triplet)
                        founded_triplets[self.create_triplet_string(triplet)] = 1
                else:
                    pairs[nums[j]] = 1

        return result