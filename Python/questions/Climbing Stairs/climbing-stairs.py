def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    dp = [0 for _ in range(n)]
    
    dp[0] = 1
    dp[1] = 2
    
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[-1]


if __name__ == "__main__":
    print(climbStairs(1))
    print(climbStairs(2))
    print(climbStairs(16))
    print(climbStairs(45))