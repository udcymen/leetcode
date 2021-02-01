class Solution:
    def maxLength(self, arr: List[str]) -> int:
        if not arr or len(arr) == 0:
            return 0
        
        combination = [set()]
        
        for word in arr:
            word_set = set(word)
            
            if len(word_set) != len(word):
                continue
                
            for c in combination:
                if c & word_set:
                    continue
                
                combination.append(c | word_set)
                
        return max([len(c) for c in combination])
                