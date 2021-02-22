class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        result = 0
        
        while Y > X:
            result += 1
            
            if Y % 2 == 0:
                Y //= 2
            else:
                Y += 1
                
        return result + X - Y