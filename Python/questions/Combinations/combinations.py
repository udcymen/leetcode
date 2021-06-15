class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        if n == None or k == None:
            return result
        
        self.dfs(n, k, 1, [], result)
        
        return result
        
    def dfs(self, n: int, k: int, level: int, path: List[int], result: List[int]) -> None:
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(level, n + 1):
            path.append(i)
            self.dfs(n, k, i + 1, path, result)
            path.pop()
