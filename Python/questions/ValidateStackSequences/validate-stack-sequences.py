class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        index = 0
        stack = []
        
        for num in pushed:
            stack.append(num)
            
            while stack and index < len(popped) and stack[-1] == popped[index]:
                stack.pop()
                index += 1
                
        return index == len(popped)