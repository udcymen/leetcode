class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        leftMostNode = root
        curr = None
        
        while leftMostNode.left:
            curr = leftMostNode
            
            while curr:
                curr.left.next = curr.right
                
                if curr.next:
                    curr.right.next = curr.next.left
                
                curr = curr.next
            
            leftMostNode = leftMostNode.left
            
        return root

