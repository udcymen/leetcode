# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        
        if not root:
            return result
        
        self.dfs(root, str(root.val), result)
        
        return result
        
        
    def dfs(self, node: Optional[TreeNode], path: str, result: List[str]):
        if not node.left and not node.right and len(path) != 0:
            result.append(path)
            return

        if node.left:
            self.dfs(node.left, path + "->" + str(node.left.val), result)
            
        if node.right:
            self.dfs(node.right, path + "->" + str(node.right.val), result)
            