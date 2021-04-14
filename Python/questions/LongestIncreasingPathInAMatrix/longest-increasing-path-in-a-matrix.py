class Solution:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        n, m = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        result = 1
        
        for i in range(n):
            for j in range(m):
                result = max(result, self.dfs(i, j, n, m, matrix, dp))
                
        return result
                
    def dfs(self, i: int, j: int, n: int, m: int, matrix: List[List[int]], dp: List[List[int]]):
        if dp[i][j] != 0:
            return dp[i][j]
        
        result = 1
        
        for dx, dy in self.directions:
            x, y =  i + dx, j + dy
            
            if -1 < x < n and -1 < y < m and matrix[i][j] < matrix[x][y]:
                result = max(result, 1 + self.dfs(x, y, n, m, matrix, dp))
        
        dp[i][j] = result
        
        return result