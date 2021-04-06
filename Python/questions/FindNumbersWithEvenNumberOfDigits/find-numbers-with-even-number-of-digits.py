class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        result = 0
        
        for num in nums:
            if len(str(num)) % 2 == 0:
                result += 1
                
        return result