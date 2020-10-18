## 187. Repeated DNA Sequences

### Question
All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA. Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

### Examples
Example 1:  
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"  
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:  
Input: s = "AAAAAAAAAAAAA"  
Output: ["AAAAAAAAAA"]

### Constraints
0 <= s.length <= 105  
s[i] is 'A', 'C', 'G', or 'T'.

### Run Environment
Python 3.9

### Time and Space Complexity:
Time: O(len(s))  
Space: O(len(s))  
Actual Time: 68 ms  
Actual Space: 27.5 MB
