class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def dfs(node: TreeNode, result: int):
    if not node:
        return 0
    
    result = 2 * result + node.val

    if not node.left and not node.right:
        return result
    else:
        return dfs(node.left, result) + dfs(node.right, result)

def sum_root_to_leaf(root: TreeNode) -> int:
    return dfs(root, 0)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)
    
    print(sum_root_to_leaf(root))
