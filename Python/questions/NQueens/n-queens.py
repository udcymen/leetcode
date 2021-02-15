class Solution:
    diagonal_one = set()
    diagonal_two = set()
    column = set()
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        self.dfs(n, [], result)
        return result
    
    def dfs(self, n: int, board: List[str], result: List[List[str]]):
        row = len(board)
        
        if row == n:
            result.append(board[:])
            return
        
        for col in range(n):
            if row + col in self.diagonal_one or row - col in self.diagonal_two or col in self.column:
                continue
                
            newRow = '.' * n

            self.diagonal_one.add(row + col)
            self.diagonal_two.add(row - col)
            self.column.add(col)

            self.dfs(n, board + [newRow[:col] + 'Q' + newRow[col + 1:]], result)

            self.diagonal_one.remove(row + col)
            self.diagonal_two.remove(row - col)
            self.column.remove(col)
        