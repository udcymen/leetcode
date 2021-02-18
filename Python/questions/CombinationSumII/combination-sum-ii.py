class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        if not candidates or not target:
            return result
        
        candidates.sort()
        self.dfs(candidates, target, 0, [], result)
        return result
    
    def dfs(self, candidates: List[int], target: int, index: int, path: List[int], result: List[List[int]]) -> None:
        if target == 0:
            result.append(path[:])
            return
            
        if target < 0:
            return
        
        for i, num in enumerate(candidates[index: ]):
            if num > target:
                break
                
            if i != 0 and candidates[index + i] == candidates[index + i - 1]:
                continue
                
            path.append(num)
            self.dfs(candidates, target - num, index + i + 1, path, result)
            path.pop()