def lengthOfLongestSubstring(s: str) -> int:
    if not s or len(s) == 0:
        return 0
    
    result = 1
    start_index = 0
    dictionary = {}
    
    for index, value in enumerate(s):
        if value in dictionary:
            start_index = max(start_index, dictionary[value] + 1)
        
        result = max(result, index - start_index + 1)
        dictionary[value] = index
            
    return result


if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))
    print(lengthOfLongestSubstring("bbbbb"))
    print(lengthOfLongestSubstring("pwwkew"))
    print(lengthOfLongestSubstring(""))