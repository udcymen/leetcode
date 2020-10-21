def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
        return False
        
    i, j = 0, len(matrix[0]) - 1
    
    while i < len(matrix) and j > -1:
        if target == matrix[i][j]:
            return True
        elif target < matrix[i][j]:
            j -= 1
        else:
            i += 1
        
    return False


if __name__ == "__main__":
    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))
    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 13))
    print(searchMatrix([], 0))
    print(searchMatrix([[]], 0))