# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        
        curr = head
        leftStart = leftCurr = ListNode()
        rightStart = rightCurr = ListNode()
        
        while curr:
            if curr.val < x:
                leftCurr.next = curr
                leftCurr = leftCurr.next
            else:
                rightCurr.next = curr
                rightCurr = rightCurr.next
                
            curr = curr.next
            
        leftCurr.next = rightStart.next
        rightCurr.next = None
        
        return leftStart.next