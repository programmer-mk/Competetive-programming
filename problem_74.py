class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occurencies = {}
        N = len(s)
        if N == 0:
            return 0
        
        start = 0
        occurencies[s[0]] = 1
        max_len = 1
        for idx in range(1,N):
            if not occurencies.get(s[idx]):
                occurencies[s[idx]] = 1
                max_len = max(max_len, idx-start+1)
            else:
                occurencies[s[idx]] += 1
                
            while occurencies[s[idx]] > 1:
                occurencies[s[start]] -= 1
                if not occurencies[s[start]]:
                    del occurencies[s[start]]
                start += 1
            
        return max_len
        