class Solution:
    def minSteps(self, n: int) -> int:
        result = 0
        factor = 2
        
        while n > 1:
            while n % factor == 0:
                result += factor
                n /= factor
                
            factor += 1
            
        return result