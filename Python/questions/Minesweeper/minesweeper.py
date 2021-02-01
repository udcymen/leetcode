class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board or not board[0] or not click or len(click) != 2:
            return board
        
        x, y = click

        if board[x][y] == 'M':
            board[x][y] = 'X'
        elif board[x][y] == 'E':
            n, m = len(board), len(board[0])
            adjacentMines = 0
            
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if i == 0 and j == 0:
                        continue
                    
                    new_x, new_y = x + i, y + j
                    
                    if self.isOutBound(new_x, new_y, n, m):
                        continue
                    
                    if board[new_x][new_y] == 'M' or board[new_x][new_y] == 'X':
                        adjacentMines += 1
                        
            if adjacentMines != 0:
                board[x][y] = str(adjacentMines)
            else:
                board[x][y] = 'B'
                
                for i in range(-1, 2, 1):
                    for j in range(-1, 2, 1):
                        if i == 0 and j == 0:
                            continue

                        new_x, new_y = x + i, y + j

                        if self.isOutBound(new_x, new_y, n, m):
                            continue

                        if board[new_x][new_y] == 'E':
                            self.updateBoard(board, [new_x, new_y])

        return board
    
    def isOutBound(self, x: int, y: int, n: int, m: int) -> bool:
        return x < 0 or x >= n or y < 0 or y >= m