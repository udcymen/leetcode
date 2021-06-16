# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        aLength, bLength = 0, 0
        aNode, bNode = headA, headB
        
        while aNode:
            aLength += 1
            aNode = aNode.next
            
        while bNode:
            bLength += 1
            bNode = bNode.next
            
        diff = aLength - bLength
        aNode, bNode = headA, headB
        
        while diff != 0:
            if diff > 0:
                aNode = aNode.next
                diff -= 1
            elif diff < 0:
                bNode = bNode.next
                diff += 1
                
        while aNode and bNode:
            if aNode == bNode:
                return aNode
            
            aNode = aNode.next
            bNode = bNode.next