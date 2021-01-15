# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.checkHeight(root) != -1

    def checkHeight(self, node: TreeNode) -> int:
        if not node:
            return 0

        left = self.checkHeight(node.left)
        right = self.checkHeight(node.right)
        
        # Use -1 Height to denote current tree is not balance
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        
        return max(left, right) + 1