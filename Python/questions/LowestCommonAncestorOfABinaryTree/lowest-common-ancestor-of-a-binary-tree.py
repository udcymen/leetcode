class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    result = None
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.findNode(root, p, q)
        return self.result
        
    def findNode(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> None:
        if not node:
            return False
        
        curr = node == p or node == q
        left = self.findNode(node.left, p, q)
        right = self.findNode(node.right, p, q)
        
        if curr + left + right > 1:
            self.result = node
        
        return curr or left or right