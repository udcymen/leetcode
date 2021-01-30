class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        length = len(s)
        s_dict = {}
        t_dict = {}
        
        for i in range(length):
            s_char = s[i]
            t_char = t[i]
            
            if s_dict.get(s_char, -1) != t_dict.get(t_char, -1):
                return False
            
            s_dict[s_char] = t_dict[t_char] = i
            
        return True