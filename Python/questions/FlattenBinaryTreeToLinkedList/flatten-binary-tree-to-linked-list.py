# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    root = None
    
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.root = root
        self.transform(root)
        
    def transform(self, node: TreeNode) -> None:
        if not node:
            return
        
        left, right = node.left, node.right
        
        if self.root != node:
            self.root.left = None
            self.root.right = node
            self.root = node
        
        self.transform(left)
        self.transform(right)
