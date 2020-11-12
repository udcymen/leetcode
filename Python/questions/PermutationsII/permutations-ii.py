from collections import Counter

class Solution:
    def dfs(self, nums: list[int], path: list[int], counter: dict, result: list[list[int]]):
        if len(nums) == len(path):
            result.append(list(path))
            return
        
        for num in counter:
            if counter[num] > 0:
                path.append(num)
                counter[num] -= 1
                
                self.dfs(nums, path, counter, result)
                
                path.pop()
                counter[num] += 1
        
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        counter = Counter(nums)
        result = []    
        
        self.dfs(nums, [], counter, result)
        
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.permuteUnique([1,1,2]))
    print(solution.permuteUnique([1,2,3]))