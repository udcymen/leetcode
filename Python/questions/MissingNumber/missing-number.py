class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return
        
        l = len(nums)
        expectSum = l * (l + 1) // 2
        actualSum = sum(nums)
        
        return expectSum - actualSum