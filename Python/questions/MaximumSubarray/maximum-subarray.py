class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxResult = float("-inf")
        tempResult = 0
        
        for num in nums:
            tempResult = tempResult + num if tempResult > 0 else num
            maxResult = tempResult if tempResult > maxResult else maxResult
            
        return maxResult