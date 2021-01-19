class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 0:
            return False
    
        target = len(nums) - 1
    
        for i in range(len(nums) - 1, -1, -1):
            if (nums[i] + i >= target):
                target = i
                
        return target == 0