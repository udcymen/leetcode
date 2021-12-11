class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        
        firstNum, secondNum, thirdNum = 0, 1, 1
        
        for _ in range(3, n + 1):
            firstNum, secondNum, thirdNum = secondNum, thirdNum, firstNum + secondNum + thirdNum
            
        return thirdNum