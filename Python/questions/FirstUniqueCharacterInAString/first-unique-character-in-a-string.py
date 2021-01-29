class Solution:
    def firstUniqChar(self, s: str) -> int:
        visited = {}
        
        for index, char in enumerate(s):
            if char in visited:
                visited[char] = -1
            else:
                visited[char] = index
                
        for value in visited.values():
            if value != -1:
                return value
            
        return -1