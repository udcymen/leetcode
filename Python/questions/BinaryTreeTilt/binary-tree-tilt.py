class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = 0
    
    def traverse(self, node: TreeNode) -> int:
        if not node:
            return 0
        
        left = self.traverse(node.left)
        right = self.traverse(node.right)

        self.result += abs(left- right)
        
        return left + right + node.val
        
    def findTilt(self, root: TreeNode) -> int:
        self.result = 0
        self.traverse(root)
        return self.result