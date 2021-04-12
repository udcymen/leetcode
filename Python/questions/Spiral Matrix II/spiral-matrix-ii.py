class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n < 1:
            return []
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        state = 0
        visited = set()
        x, y = 0, 0
        result = [[0 for _ in range(n)] for _ in range(n)]
        num = 0
        
        while num < n * n:
            num += 1
            result[x][y] = num
            visited.add((x, y))
            dx, dy = directions[state]
            new_x, new_y = x + dx, y + dy
            
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n or (new_x, new_y) in visited:
                state = (state + 1) % len(directions)
                dx, dy = directions[state]
                new_x, new_y = x + dx, y + dy

            x, y = new_x, new_y
                    
        return result