"""
All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". 
When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.


Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

0 <= s.length <= 105
s[i] is 'A', 'C', 'G', or 'T'.


Run Envrioment:
Python 3.9


Time and Space Complexity:
Time: O(len(s))
Space: O(len(s))
Actual Time: 68 ms
Space: 27.5 MB
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