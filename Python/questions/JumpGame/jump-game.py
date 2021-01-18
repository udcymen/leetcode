class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 0:
            return False
    
        n = len(nums)
    
        dp = [False for _ in range(n)]
        dp[0] = True
        
        for i in range(1, n):
            for j in range(i, -1, -1):
                if dp[j] and nums[j] + j >= i:
                    dp[i] = True
                    break

                               
        return dp[n - 1]