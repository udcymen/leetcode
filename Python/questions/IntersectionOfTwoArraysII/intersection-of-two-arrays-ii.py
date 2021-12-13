from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictionary = {}
        
        result = []
        
        for num in nums1:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] += 1
            
        for num in nums2:
            if num in dictionary and dictionary[num] > 0:
                result.append(num)
                dictionary[num] -= 1
                
        return result