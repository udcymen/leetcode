class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        result = -1
        
        if not nums or len(nums) == 0:
            return result
        
        l = len(nums)
        prefix = 0
        prefix_sum = [prefix]
        
        for num in nums:
            prefix += num
            prefix_sum.append(prefix)
            
        index = 0
        
        while index < l:
            leftSum = prefix_sum[index]
            rightSum = prefix_sum[l] - prefix_sum[index + 1]
            
            if leftSum == rightSum:
                return index
            
            index += 1
        
        return result