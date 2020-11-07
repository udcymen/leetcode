class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    result = tmp = ListNode(0)
    carry = 0
    
    while l1 and l2:
        total = l1.val + l2.val + carry
        tmp.next = ListNode(total % 10)
        carry = total // 10
        tmp = tmp.next
        l1 = l1.next
        l2 = l2.next
    
    while l1:
        total = l1.val + carry
        tmp.next = ListNode(total % 10)
        carry = total // 10
        tmp = tmp.next
        l1 = l1.next
        
    while l2:
        total = l2.val + carry
        tmp.next = ListNode(total % 10)
        carry = total // 10
        tmp = tmp.next
        l2 = l2.next
        
    if carry != 0:
        tmp.next = ListNode(carry)
    
    return result.next