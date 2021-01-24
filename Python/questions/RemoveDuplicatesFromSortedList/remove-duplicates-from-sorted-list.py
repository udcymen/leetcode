# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prevNode = None
        currNode = head
        
        while currNode:
            if prevNode and currNode.val == prevNode.val:
                prevNode.next = currNode.next
            else:
                prevNode = currNode
                
            currNode = currNode.next                
        
        return head
    