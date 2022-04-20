class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {}
        
        def can_jump_helper(index):
            if index > len(nums)-1:
                return False
            elif index == len(nums)-1:
                return True
            elif dp.get(index) is not None:
                return dp[index]
            elif nums[index] == 0:
                return False
            else:
                for offset in range(1, nums[index]+1):
                    if can_jump_helper(index+offset):
                        dp[index] = True
                        return True
                dp[index] = False
                return False
            
        return can_jump_helper(0)
            