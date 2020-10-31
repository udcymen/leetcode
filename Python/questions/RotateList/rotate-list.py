class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head:
        return head
    
    count = 1
    start, end = head, head
    
    while end.next:
        end = end.next
        count += 1

    k %= count

    if k == 0:
        return head
    
    for i in range(count - k - 1):
        start = start.next
        
    result = start.next
    start.next = None
    end.next = head
    
    return result