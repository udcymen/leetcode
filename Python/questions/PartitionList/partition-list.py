# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lessNode = lessCurr = ListNode()
        greatNode = greatCurr = ListNode()
        curr = head
        
        while curr:
            if curr.val < x:
                nextNode = curr.next
                curr.next = None
                lessCurr.next = curr
                lessCurr = curr
                curr = nextNode
            else:
                nextNode = curr.next
                curr.next = None
                greatCurr.next = curr
                greatCurr = curr
                curr = nextNode
                
        if not lessNode.next:
            return greatNode.next
        
        lessCurr.next = greatNode.next
        
        return lessNode.next