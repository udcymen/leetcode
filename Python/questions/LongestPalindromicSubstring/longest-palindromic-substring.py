def getLongestPalindrome(start: int, end: int, s: str) -> str:
        while start > -1 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
            
        return s[start + 1:end]
        
def longestPalindrome(s: str) -> str:
    if not s or len(s) == 0:
        return ""
    
    if len(s) == 1:
        return s
    
    result = ""
    
    for index in range(len(s)):
        odd = getLongestPalindrome(index, index, s)
        even = getLongestPalindrome(index, index + 1, s)
        
        if len(odd) > len(result):
            result = odd
            
        if len(even) > len(result):
            result = even
            
    return result


if __name__ == "__main__":
    print(longestPalindrome("babad"))
    print(longestPalindrome("cbbd"))
    print(longestPalindrome("a"))
    print(longestPalindrome("ac"))
    print(longestPalindrome("bb"))