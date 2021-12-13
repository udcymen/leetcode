from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        
        for i, num in enumerate(nums):
            if num in dictionary:
                return [dictionary[num], i]
            
            dictionary[target - num] = i
        