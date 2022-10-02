class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [] 
        
        if not nums or len(nums) == 0:
            return result
        
        prefix = 0
        
        for num in nums:
            prefix += num
            result.append(prefix)
            
        return result