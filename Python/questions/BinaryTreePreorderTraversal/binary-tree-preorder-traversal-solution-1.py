class TreeNode:
    def __init__(self, val:int = 0, left:'TreeNode' = None, right:'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: Recursion
def traversal(node: TreeNode, result: list[int]):
    if not node:
        return
    
    result.append(node.val)
    traversal(node.left, result)
    traversal(node.right, result)
        
def preorderTraversal(root: TreeNode) -> list[int]:
    result = []
    
    traversal(root, result)

    return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print(preorderTraversal(root))