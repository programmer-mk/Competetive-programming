class Solution:
    
    def numDecodings(self, s: str) -> int:
        vals=[str(i) for i in range(1,27)]
        n=len(s)
        
        @lru_cache(None)
        def dp(i):
            if i==n:
                return 1
            res=0
            
            if s[i:i+1] in vals:
                res+=dp(i+1)
            if s[i:i+2] in vals:
                res+=dp(i+2)
            return res
        
        return dp(0)