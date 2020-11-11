class Solution:
    def flipAndInvertImage(self, matrix: list[list[int]]) -> list[list[int]]:
        if not matrix or len(matrix) == 0:
            return matrix
        
        for row in matrix:
            start, end = 0, len(row) - 1

            while start < end:
                if row[start] == row[end]:
                    row[start], row[end] = 1 - row[start], 1 - row[end]
                
                start += 1
                end -= 1
                
            if start == end:
                row[start] = 1 - row[start]
                    
        return matrix


if __name__ == "__main__":
    solution = Solution()
    print(solution.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
    print(solution.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))