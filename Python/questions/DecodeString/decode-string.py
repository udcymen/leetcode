class Solution:
    def decodeString(self, s: str) -> str:
        stack = [""]
        repeat = 0
        
        for char in s:
            if char.isdigit():
                repeat = repeat * 10 + int(char)
            elif char == '[':
                stack.append(repeat)
                stack.append("")
                repeat = 0
            elif char == ']':
                chars = stack.pop()
                times = stack.pop()
                stack[-1] += chars * times
            else:
                stack[-1] += char
            
        return "".join(stack)


if __name__ == "__main__":
    solution = Solution()
    print(solution.decodeString("3[a]2[bc]"))
    print(solution.decodeString("3[a2[c]]"))
    print(solution.decodeString("2[abc]3[cd]ef"))
    print(solution.decodeString("abc3[cd]xyz"))