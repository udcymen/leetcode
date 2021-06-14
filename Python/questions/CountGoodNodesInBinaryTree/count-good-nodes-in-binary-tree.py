# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    result = 0
    
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0
        self.countNodes(root, -sys.maxsize - 1)
        return self.result
        
    def countNodes(self, node: TreeNode, parentMax: int) -> None:
        if not node:
            return
        
        if node.val >= parentMax:
            parentMax = node.val
            self.result += 1
            
        self.countNodes(node.left, parentMax)
        self.countNodes(node.right, parentMax)