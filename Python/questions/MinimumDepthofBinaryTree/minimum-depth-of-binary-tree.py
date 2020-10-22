class TreeNode:
    def __init__(self, val:int = 0, left:'TreeNode' = None, right:'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right
        

def minDepth(root: TreeNode) -> int:
    if root == None:
        return 0
    
    left = minDepth(root.left)
    right = minDepth(root.right)
    
    
    if left == 0:
        return right + 1
    
    if right == 0:
        return left + 1
    
    
    return min([left, right]) + 1


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    print(minDepth(root))