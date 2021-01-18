class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        
        n = len(triangle)
        
        dp = triangle[-1]
        
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
            
        return dp[0]