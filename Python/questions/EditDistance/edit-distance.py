class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        
        if len(word2) == 0:
            return len(word1)
        
        n, m = len(word1), len(word2)
        
        dp = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
        
        dp[0][0] = 0
        
        for i in range(n + 1):
            dp[i][0] = i
            
        for j in range(m + 1):
            dp[0][j] = j
            
        print(dp)
        
        # dp[i - 1][j] -> Insert
        # dp[i][j - 1] -> Delete
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                c = 0 if word1[i - 1] == word2[j - 1] else 1
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + c)
                    
        return dp[n][m]