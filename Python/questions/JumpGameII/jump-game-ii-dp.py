class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        n = len(nums)
        dp = [float('inf') for _ in range(n)]
        
        dp[0] = 0
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] + j >= i:
                    dp[i] = dp[j] + 1
                    break

        return dp[n - 1]