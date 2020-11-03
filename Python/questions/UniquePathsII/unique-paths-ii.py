def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    if obstacleGrid[0][0] == 1:
        return 0

    dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
    
    for i in range(len(obstacleGrid)):
        if obstacleGrid[i][0] == 1:
            break
        
        dp[i][0] = 1

    for j in range(len(obstacleGrid[0])):
        if obstacleGrid[0][j] == 1:
            break
            
        dp[0][j] = 1
            
    for i in range(1, len(obstacleGrid)):
        for j in range(1, len(obstacleGrid[0])):
            if obstacleGrid[i][j] == 1:
                continue
                
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]


if __name__ == "__main__":
    print(uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))
    print(uniquePathsWithObstacles([[0,0],[0,1],[0,0]]))
    print(uniquePathsWithObstacles([[1,0]]))