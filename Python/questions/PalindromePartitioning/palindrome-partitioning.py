class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        self.dfs(s, 0, [], result)
        return result
        
    def dfs(self, s: str, start: int, path: list[str], result: list[list[str]]) -> None:
        if start >= len(s):
            result.append(path[:])
            return
        
        for end in range(start, len(s)):
            if self.isPalindrome(s, start, end):
                path.append(s[start: end + 1])
                self.dfs(s, end + 1, path, result)
                path.pop()
            
    def isPalindrome(self, s: str, start: int, end: int) -> bool:
        while start < end:
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1
            
        return True