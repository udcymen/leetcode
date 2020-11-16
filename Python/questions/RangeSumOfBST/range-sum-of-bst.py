class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        result = 0
        
        if not root:
            return result
        
        if low <= root.val <= high:
            result += root.val
            
        if low <= root.val:
            result += self.rangeSumBST(root.left, low, high)
            
        if root.val <= high:
            result += self.rangeSumBST(root.right, low, high)

        return result

