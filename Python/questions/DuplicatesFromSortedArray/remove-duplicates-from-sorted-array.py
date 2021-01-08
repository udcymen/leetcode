class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        index = 0
        
        for j in range(1, len(nums)):
            if nums[j] != nums[index]:
                index += 1
                nums[index] = nums[j]
                
        return index + 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates([1,1,2]))
    print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))