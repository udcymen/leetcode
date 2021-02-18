class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or not target:
            return []
        
        result = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], result)
        return result
        
        
    def dfs(self, candidates: List[int], target: int, index: int, path: List[int], result: List[List[int]]) -> None:
        if target == 0:
            result.append(path[:])
            return
            
        if target < 0:
            return
        
        for i, num in enumerate(candidates[index:]):
            path.append(num)
            self.dfs(candidates, target - num, index + i, path, result)
            path.pop()