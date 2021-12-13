from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1, index2 = m - 1, n - 1
        index = n + m - 1
        
        while index1 > -1 and index2 > -1:
            num1, num2 = nums1[index1], nums2[index2]
            
            if num1 > num2:
                nums1[index] = num1
                index1 -= 1
            else:
                nums1[index] = num2
                index2 -= 1
                
            index -= 1
        
        while index2 > -1:
            nums1[index] = nums2[index2]
            index2 -= 1
            index -= 1
            