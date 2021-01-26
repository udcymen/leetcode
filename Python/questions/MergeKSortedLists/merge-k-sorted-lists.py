from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        
        result = curr = ListNode(0)
        q = PriorityQueue()
        
        for index, head in enumerate(lists):
            if head:
                q.put((head.val, index, head))

        while not q.empty():
            _, index, node = q.get()
            curr.next = node
            curr = node
            
            if curr.next:
                q.put((curr.next.val, index, curr.next))
            
        return result.next