class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        
        for index, num in enumerate(nums):
            start, end = index + 1, len(nums) - 1
            
            
            while start < end:
                total = num + nums[start] + nums[end]
                
                if total == target:
                    return target
                
                if abs(target - total) < abs(diff):
                    diff = target - total

                if total < target:
                    start += 1
                else:
                    end -= 1
                    
        return target - diff