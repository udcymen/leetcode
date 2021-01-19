class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        result, target, nextTarget = 0, 0, 0
        
        for i in range(len(nums) - 1):
            nextTarget = max(nextTarget, i + nums[i])
            
            if i == target:
                result += 1
                target = nextTarget

        return result