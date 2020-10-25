class TreeNode:
    def __init__(self, val:int = 0, left:'TreeNode' = None, right:'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


# Solution 2: Iterative
def preorderTraversal(root: TreeNode) -> list[int]:
    result = []
        
    if not root:
        return result
    
    stack = [root]
    
    while stack:
        node = stack.pop()
        
        while node:
            result.append(node.val)
            
            if node.right:
                stack.append(node.right)
                
            node = node.left

    return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print(preorderTraversal(root))