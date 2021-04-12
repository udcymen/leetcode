class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for c in path.split("/"):
            if c == "/" or c == "." or c == "":
                continue
            elif c == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
                
        return "/" + "/".join(stack)