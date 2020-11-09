class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traversal(node: TreeNode, high: int, low: int) -> int:
    if not node:
        return high - low
    
    high = max(high, node.val)
    low = min (low, node.val)
    
    return max(traversal(node.left, high, low), traversal(node.right, high, low))
    
def maxAncestorDiff(root: TreeNode) -> int:
    return traversal(root, root.val, root.val)


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(0)
    root.right.right.left = TreeNode(3)
    print(maxAncestorDiff(root))