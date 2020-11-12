class Solution:
    def dfs(self, nums: list[int], path: list[int], result: list[list[int]]):
        if not nums:
            return result.append(path)
        
        for index, value in enumerate(nums):
            self.dfs(nums[:index] + nums[index + 1:], path + [value], result)
        
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        self.dfs(nums, [], result)
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.permute([1,2,3]))