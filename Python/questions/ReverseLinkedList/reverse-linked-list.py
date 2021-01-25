# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        prevNode = None
        
        while head:
            nextNode = head.next
            head.next = prevNode
            prevNode = head
            head = nextNode

        return prevNode