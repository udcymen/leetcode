# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        val = float('-inf')
        stack = []
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
                
            if val >= root.val:
                return False
            
            val = root.val
            root = root.right
            
        return True