from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == None or len(nums) == 0:
            return -1
        
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            num = nums[mid]
            
            if num == target:
                return mid
            elif num < target:
                start = mid
            else:
                end = mid
                
        if nums[start] == target:
            return start
        
        if nums[end] == target:
            return end
        
        return -1