class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    result1, result2 = 0, 0
    
    while l1:
        result1 = result1 * 10 + l1.val
        l1 = l1.next
        
    while l2:
        result2 = result2 * 10 + l2.val
        l2 = l2.next
        
    digits = str(result1 + result2)
    dummy = ListNode()
    start = dummy
    
    for d in digits:
        start.next = ListNode(int(d))
        start = start.next
        
    return dummy.next