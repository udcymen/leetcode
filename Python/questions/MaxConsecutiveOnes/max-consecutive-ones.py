class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        
        if not nums or len(nums) == 0:
            return result
        
        localResult = 0
        
        for num in nums:
            if num == 0:
                result = max(result, localResult)
                localResult = 0
            else:
                localResult += 1
        
        return max(result, localResult)