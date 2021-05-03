class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        aLen = len(s1)
        bLen = len(s2)
        
        if aLen > bLen:
            return False
        
        aDict = dict.fromkeys(string.ascii_lowercase, 0)
        bDict = dict.fromkeys(string.ascii_lowercase, 0)
        
        for c in s1:
            aDict[c] = aDict[c] + 1
            
        for i in range(bLen):
            new_c = s2[i]
            bDict[new_c] = bDict[new_c] + 1
            
            if i >= aLen:
                old_c = s2[i - aLen]
                bDict[old_c] = bDict[old_c] - 1

            if aDict == bDict:
                return True
            
        return False