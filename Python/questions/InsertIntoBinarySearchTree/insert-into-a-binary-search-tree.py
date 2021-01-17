# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        newNode = TreeNode(val)
        
        if not root:
            return newNode
        
        node = root
        
        while node:
            if node.val > val:
                if not node.left:
                    node.left = newNode
                    break
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = newNode
                    break
                else:
                    node = node.right
                    
        return root
