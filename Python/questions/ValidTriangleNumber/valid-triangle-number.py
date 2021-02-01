class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if not nums or len(nums) < 3:
            return 0
        
        nums.sort()
        n = len(nums)
        result = 0
        
        for i in range(n - 1, 1, -1):
            start = 0
            end = i - 1
            
            while start < end:
                if nums[start] + nums[end] > nums[i]:
                    result += (end - start)
                    end -= 1
                else:
                    start += 1
                    
        return result