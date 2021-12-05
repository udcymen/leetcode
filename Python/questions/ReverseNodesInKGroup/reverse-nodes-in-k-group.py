from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        node = head
        
        while node and count != k:
            node = node.next
            count += 1
            
        if count == k:
            reverseHead = self.reverse(head, k)
            head.next = self.reverseKGroup(node, k)
            head = reverseHead

        return head
               
    def reverse(self, node: Optional[ListNode], k: int) -> Optional[ListNode]:
        prevNode = None
        
        for _ in range(k):
            
            nextNode = node.next
            node.next = prevNode
            prevNode = node
            node = nextNode

        return prevNode