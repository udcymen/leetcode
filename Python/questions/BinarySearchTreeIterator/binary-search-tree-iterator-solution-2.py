class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        
        self.getLeftMostNode(root)
        
    def getLeftMostNode(self, node: TreeNode) -> None:
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        
        if node.right:
            self.getLeftMostNode(node.right)
            
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0


if __name__ == "__main__":
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    iterator = BSTIterator(root)
    print(iterator.next());    # return 3
    print(iterator.next());    # return 7
    print(iterator.hasNext()); # return true
    print(iterator.next());    # return 9
    print(iterator.hasNext()); # return true
    print(iterator.next());    # return 15
    print(iterator.hasNext()); # return true
    print(iterator.next());    # return 20
    print(iterator.hasNext()); # return false