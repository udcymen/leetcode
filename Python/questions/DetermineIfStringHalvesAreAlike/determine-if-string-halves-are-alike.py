class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        if not s or len(s) == 0:
            return 0
        
        vowels = { 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' }
        numVowels = 0
        mid = len(s) // 2
        
        for index, c in enumerate(s):
            if index < mid:
                if c in vowels:
                    numVowels += 1
            else:
                if c in vowels:
                    numVowels -= 1
        
        return numVowels == 0