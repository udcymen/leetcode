class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict or len(wordDict) == 0:
            return False
        
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j: i] in wordDict:
                    dp[i] = True

        return dp[n]