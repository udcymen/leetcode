class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        
        if not words or not pattern:
            return result
        
        for word in words:
            mapping = {}
            isMapped = True
            
            for i, c in enumerate(word):
                p = pattern[i]
                
                if p in mapping and mapping[p] != c:
                    isMapped = False
                    break
                    
                mapping[p] = c
                
            values = mapping.values()
            
            if len(values) != len(set(values)):
                isMapped = False
                
            if isMapped:
                result.append(word)
                
        return result