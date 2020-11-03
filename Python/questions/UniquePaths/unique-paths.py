def uniquePaths(m: int, n: int) -> int:
    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(m):
        dp[0][i] = 1
        
    for j in range(n):
        dp[j][0] = 1
        
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]


if __name__ == "__main__":
    print(uniquePaths(3, 7))
    print(uniquePaths(3, 2))
    print(uniquePaths(7, 3))
    print(uniquePaths(3, 3))