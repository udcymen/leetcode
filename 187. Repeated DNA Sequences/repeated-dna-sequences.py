"""
Run Envrioment:
Python 3.9

Time and Space Complexity:
Time: O(len(s))
Space: O(len(s))
Actual Time: 68 ms
Actual Space: 27.5 MB
"""

from collections import Counter

def findRepeatedDnaSequences(s: str) -> list[str]:
        if len(s) < 10:
            return []
        
        counter = Counter(s[i: i + 10] for i in range(len(s) - 10 + 1))
        
        return [key for key in counter if counter[key] > 1]


if __name__ == "__main__":
    print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    print(findRepeatedDnaSequences("AAAAAAAAAAAAA"))