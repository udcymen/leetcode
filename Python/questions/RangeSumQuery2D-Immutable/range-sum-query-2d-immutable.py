class NumMatrix:
    dp = []
    
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        
        n, m = len(matrix), len(matrix[0])

        self.dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                self.dp[i + 1][j + 1] = self.dp[i + 1][j]  + self.dp[i][j + 1] - self.dp[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row2 + 1][col1] - self.dp[row1][col2 + 1] + self.dp[row1][col1]