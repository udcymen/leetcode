class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getDecimalValue(head: ListNode) -> int:
    result = 0
    
    while head:
        result = result * 2 + head.val
        head = head.next
        
    return result


if __name__ == "__main__":
   head = ListNode(1)
   head.next = ListNode(0)
   head.next.next = ListNode(1)
   print(getDecimalValue(head))