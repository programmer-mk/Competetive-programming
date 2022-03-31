class Solution:
    
    def longest_common_subsequence_recursive(self, text1, text2, idx1, idx2, dp) -> int:
        #print(f'indexes: {idx1}, {idx2}')
        if idx1 == len(text1) or idx2 == len(text2):
            return 0
        elif dp[idx1][idx2] != -1:
            result = dp[idx1][idx2]
        elif text1[idx1] == text2[idx2]:
            result = 1 + self.longest_common_subsequence_recursive(text1, text2, idx1+1, idx2+1, dp)
        else:
            result = max(self.longest_common_subsequence_recursive(text1, text2, idx1+1, idx2, dp), \
                      self.longest_common_subsequence_recursive(text1, text2, idx1, idx2+1, dp))
        
        dp[idx1][idx2] = result
        return result
        
    
    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        return self.longest_common_subsequence_recursive(text1, text2, 0, 0, dp)