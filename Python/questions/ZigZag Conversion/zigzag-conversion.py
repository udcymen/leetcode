# numRows = 1, 2, 3, 4, 5, 6 ...
# Gap     = 1, 2, 4, 6, 8, 10 ...
    
def convert(s: str, numRows: int) -> str:
    if not s or len(s) == 0:
        return ""
    
    if numRows == 1:
        return s
    
    result = ""
    gap = 2 * (numRows - 1)
    
    for row in range(numRows):
        start = 0
        
        while start + row < len(s):
            result += s[row + start]
            
            if row != 0 and row != numRows - 1 and (start + gap - row) < len(s):
                result += s[start + gap - row]
            
            start += gap
        
    return result


if __name__ == "__main__":
    print(convert("PAYPALISHIRING", 1))
    print(convert("PAYPALISHIRING", 3))
    print(convert("PAYPALISHIRING", 4))
    print(convert("A", 1))