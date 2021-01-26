# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        node_dict = {}
        result = curr = Node(0)
        node = head
        
        while node:
            curr.next = Node(node.val)
            curr = curr.next
            node_dict[node] = curr
            node = node.next
            
        node = head
        curr = result.next

        while node:
            if node.random:
                curr.random = node_dict[node.random]
            node = node.next
            curr = curr.next
        
        return result.next