# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        
        return self.ListToTree(head, None)
        
    def ListToTree(self, head: ListNode, tail: ListNode) -> TreeNode:
        if head == tail:
            return None
        
        slow, fast = head, head
        
        while fast != tail and fast.next != tail:
            slow = slow.next
            fast = fast.next.next
        
        result = TreeNode(slow.val)
        result.left = self.ListToTree(head, slow)
        result.right = self.ListToTree(slow.next, tail)
        
        return result
        