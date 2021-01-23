class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        n, m = len(s1), len(s2)
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        
        dp[0][0] = True
        
        for i in range(1, n + 1):
            if s3.startswith(s1[:i]):
                dp[i][0] = True
                
        for j in range(1, m + 1):
            if s3.startswith(s2[:j]):
                dp[0][j] = True
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
                
                if s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]
                    
        return dp[n][m]