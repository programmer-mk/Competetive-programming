class Solution:

    def valid_candidates(self, state, nums):
        return list(set(nums) - set(state))

    def valid_state(self, state, nums):
        if len(set(state)) == len(nums):
            return True
        else:
            return False

    def search(self, state, nums, result):
        if self.valid_state(state, nums):
            result.append(state.copy())

        if len(state) < len(nums):
            candidates = self.valid_candidates(state, nums)
            for candidate in candidates:
                state.append(candidate)
                self.search(state, nums, result)
                state.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        state = []
        result = []
        self.search(state, nums, result)
        return result
