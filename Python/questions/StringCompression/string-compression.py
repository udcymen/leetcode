class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        l = len(chars)
        
        if l == 1:
            return 1
        
        slow, fast, result = 0, 0, 0

        while slow < l:
            c = chars[slow]

            while fast < l and chars[fast] == c:
                fast += 1

            chars[result] = c
            result += 1
                
            if fast > slow + 1:
                for nc in str(fast - slow):
                    chars[result] = nc
                    result += 1

            slow, fast = fast, fast + 1

        return result