from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lastRow = [1]
        result = [lastRow]
        
        if numRows == 1:
            return result
        
        for i in range(numRows - 1):
            newRow = [1]

            for i in range(1, len(lastRow)):
                newRow.append(lastRow[i] + lastRow[i - 1])
                
            newRow.append(1)
            result.append(newRow)
            lastRow = newRow
                
        return result
        