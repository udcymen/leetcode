class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertionSortList(head: ListNode) -> ListNode:
    result = ListNode()
    curr = head
    
    while curr:
        prev_node, next_node = result, result.next
        
        while next_node:
            if curr.val < next_node.val:
                break
                
            prev_node = next_node
            next_node = next_node.next
            
        temp = curr.next
        prev_node.next = curr
        curr.next = next_node
        curr = temp
    
    return result.next
        