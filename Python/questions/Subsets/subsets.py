class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        self.dfs(nums, [], 0, result)
        return result
        
    def dfs(self, nums: list[int], path: list[int], index: int, result: list[list[int]]) -> None:
        result.append(path[:])
            
        for i, num in enumerate(nums[index:]):
            self.dfs(nums, path + [num], index + i + 1, result)