class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nums = []
        self.index = -1
        
        self.travesalInOrder(root)
        
    def travesalInOrder(self, node: TreeNode) -> None:
        if not node:
            return
        
        self.travesalInOrder(node.left)
        self.nums.append(node.val)
        self.travesalInOrder(node.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.nums[self.index]
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index + 1 < len(self.nums)
        

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