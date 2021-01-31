class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        n, m = len(grid), len(grid[0])
        result = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    result += 1
                    self.dfs(i, j, n, m, grid)

        return result
    
    def dfs(self, i: int, j: int, n: int, m: int, grid: List[List[str]]) -> None:
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != "1":
            return
        
        grid[i][j] = "#"
        self.dfs(i + 1, j, n, m, grid)
        self.dfs(i, j + 1, n, m, grid)
        self.dfs(i - 1, j, n, m, grid)
        self.dfs(i, j - 1, n, m, grid)