class Solution:
    dictionary = {
        "2": "abc", "3": "def", 
        "4": "ghi", "5": "jkl", "6": "mno", 
        "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or len(digits) == 0:
            return ""
        
        result = [""]
        
        for d in digits:
            result = [r + c for c in self.dictionary[d] for r in result]
                
        return result