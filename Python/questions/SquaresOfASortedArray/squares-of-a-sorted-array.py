class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 0:
            return []
        
        result = collections.deque()
        index = len(nums) - 1
        left, right = 0, len(nums) - 1
        
        while index > -1:
            i, j = nums[left], nums[right]
            
            if abs(i) < abs(j):
                result.appendleft(j * j)
                right -= 1
            else:
                result.appendleft(i * i)
                left += 1
                
            index -= 1
                
        return list(result)