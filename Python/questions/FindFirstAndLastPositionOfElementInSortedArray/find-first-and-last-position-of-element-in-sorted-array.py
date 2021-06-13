class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target == None:
            return [-1, -1]

        length = len(nums)
        
        return [self.findFirstPostion(nums, target, length), self.findLastPostion(nums, target, length)]
        
    def findFirstPostion(self, nums: List[int], target: int, length: int) -> int:
        start, end = 0, length - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            num = nums[mid]

            if num < target:
                start = mid
            else:
                end = mid
                
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1
        
    def findLastPostion(self, nums: List[int], target: int, length: int) -> int:
        start, end = 0, length - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            num = nums[mid]
            
            if num <= target:
                start = mid
            else:
                end = mid
                
        if nums[end] == target:
            return end
        elif nums[start] == target:
            return start
        else:
            return -1
            