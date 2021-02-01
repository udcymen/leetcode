class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        
        if not s or not t:
            return False
        
        if len(s) != len(t):
            return False
        
        char_dict = {}
        
        for c in s:
            char_dict[c] = char_dict.get(c, 0) + 1
            
        for c in t:
            if c not in char_dict or char_dict[c] < 1:
                return False
            
            char_dict[c] = char_dict[c] - 1
            
        return True