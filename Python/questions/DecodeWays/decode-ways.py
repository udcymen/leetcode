class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        prevChar = s[0]
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 0 if prevChar == '0' else 1

        for i in range(2, n + 1):
            char = s[i - 1]
            first = int(char)
            second = int(prevChar + char)
            
            if 1 <= first <= 9:
                dp[i] += dp[i - 1]
            
            if 10 <= second <= 26:
                dp[i] += dp[i - 2]
                
            prevChar = char
            
        return dp[n]