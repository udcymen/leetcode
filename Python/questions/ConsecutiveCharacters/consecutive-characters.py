def maxPower(s: str) -> int:
    if not s or len(s) == 0:
        return 0
    
    result = 1
    temp_result = 1
    curr = s[0]
    
    for c in s[1:]:
        if c == curr:
            temp_result += 1
        else:
            result = max(result, temp_result)
            temp_result = 1
            curr = c
            
    return max(result, temp_result)


if __name__ == "__main__":
    print(maxPower("leetcode"))
    print(maxPower("abbcccddddeeeeedcba"))
    print(maxPower("triplepillooooow"))
    print(maxPower("hooraaaaaaaaaaay"))
    print(maxPower("tourist"))