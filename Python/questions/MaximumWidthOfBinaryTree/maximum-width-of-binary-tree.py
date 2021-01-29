# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.ids = []
        return self.dfs(root, 0, 0)
        
    def dfs(self, node: TreeNode, nodeId: int, level: int) -> int:
        if not node:
            return 0
        
        if level == len(self.ids):
            self.ids.append(nodeId)
            
        parentId = nodeId - self.ids[level]    
        
        return max(parentId + 1, self.dfs(node.left, parentId * 2, level + 1), self.dfs(node.right, parentId * 2 + 1, level + 1))