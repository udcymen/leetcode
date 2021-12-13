from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        
        for i, num in enumerate(nums):
            if num != 0:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1