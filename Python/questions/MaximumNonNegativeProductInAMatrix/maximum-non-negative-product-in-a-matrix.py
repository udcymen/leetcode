class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        n, m = len(grid), len(grid[0])
        dp = [[(float("-inf"), float("-inf")) for _ in range(m)] for _ in range(n)]
        dp[0][0] = (1, 1)
        
        for i in range(n):
            for j in range(m):
                num = grid[i][j]
                
                if i == 0 and j == 0:
                    dp[i][j] = (num, num)
                elif i == 0:
                    a, b = dp[i][j - 1]
                    dp[i][j] = (a * num, b * num)
                elif j == 0:
                    a, b = dp[i - 1][j]
                    dp[i][j] = (a * num, b * num)
                else:
                    a, b = dp[i - 1][j]
                    c, d = dp[i][j - 1]
                    
                    minNum = num * min(b, d)
                    maxNum = num * max(a, c)

                    dp[i][j] = (max(minNum, maxNum), min(minNum, maxNum))
                
        maxResult, minResult = dp[n - 1][m - 1]

        if maxResult < 0:
            return -1
                
        return maxResult % (10 ** 9 + 7)