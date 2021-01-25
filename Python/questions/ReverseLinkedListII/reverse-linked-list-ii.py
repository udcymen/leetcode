# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        
        prevNode, curr = None, head
        while m > 1:
            prevNode = curr
            curr = curr.next
            m -= 1
            n -= 1
            
        prevTargetNode = prevNode
        targetNode = curr
        
        while n > 0:
            nextNode = curr.next
            curr.next = prevNode
            prevNode = curr
            curr = nextNode
            n -= 1
            
        if prevTargetNode:
            prevTargetNode.next = prevNode
        else:
            head = prevNode
            
        targetNode.next = curr
            
        return head
        
            
        