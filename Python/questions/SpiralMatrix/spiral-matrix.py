class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        state = 0
        n, m = len(matrix), len(matrix[0])
        visited = set()
        x, y = 0, 0
        result = []
        
        while len(result) < n * m:
            result.append(matrix[x][y])
            visited.add((x, y))
            dx, dy = directions[state]
            new_x, new_y = x + dx, y + dy
            
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m or (new_x, new_y) in visited:
                state = (state + 1) % len(directions)
                dx, dy = directions[state]
                new_x, new_y = x + dx, y + dy

            x, y = new_x, new_y
                    
        return result
