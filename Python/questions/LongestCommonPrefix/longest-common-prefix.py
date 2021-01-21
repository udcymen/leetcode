class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        minLength = float('inf')
        result = ""
        
        for s in strs:
            minLength = min(minLength, len(s))
            
        for i in range(minLength):
            firstWordChar = strs[0][i]
            
            for s in strs:
                if s[i] != firstWordChar:
                    return result
            
            result += firstWordChar
            
        return result