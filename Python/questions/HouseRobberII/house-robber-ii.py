from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == None or len(nums) == 0:
            return 0
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)
        
        return max(self.helper(nums[1:]), self.helper(nums[:n - 1]))
        
    def helper(self, nums: List[int]) -> int:
        if nums == None or len(nums) == 0:
            return 0
        
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
            
        return dp[n]
        