class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertionSortList(head: ListNode) -> ListNode:
    if not head:
        return None
    
    start, end, curr = head, head, head.next
    start.next = None
    end.next = None

    while curr:
        # Insert at head
        if curr.val < start.val:
            temp = curr.next
            curr.next = start
            start = curr
            curr = temp
            continue

        stepper = start

        while stepper != end and stepper.next and stepper.next.val < curr.val:
            stepper = stepper.next
        
        # Insert at end
        if stepper == end:
            temp = curr.next
            curr.next = None
            end.next = curr
            end = curr
            curr = temp
        # Insert at mid
        else:
            temp = curr.next
            stepperTemp = stepper.next
            stepper.next = curr
            curr.next = stepperTemp
            curr = temp
        
        
    return start
        