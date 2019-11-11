class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    result = None
    head = None
    while l1 is not None and l2 is not None:
        first = ListNode(l1.val)
        second = ListNode(l2.val)
        if first.val< second.val:
            temp = first
            temp2 = second
        else:
            temp = second
            temp2 = first

        if result is None:
            result = temp
            head = result
            result.next = temp2
            result = result.next

        else:
            result.next = temp
            result = result.next
            result.next = temp2
            result = result.next

        l1 = l1.next
        l2 = l2.next

    while l1 is not None:
        temp = ListNode(l1.val)
        if result is None:
            result = temp
            head = result

        else:
            result.next = temp
            result = result.next
        l1 = l1.next

    while l2 is not None:
        temp = ListNode(l2.val)
        if result is None:
            result = temp
            head = result
        else:
            result.next = temp
            result = result.next
        l2 = l2.next
    return head


def createLinkedList(input):
    if len(input) == 0:
        return None
    head = ListNode(input[0])
    curr = head

    for i in range(1, len(input)):
        temp = ListNode(input[i])
        curr.next = temp
        curr = curr.next
    return head

def printLinkedList(head):
    all_elem = []
    start = head
    while start is not None:
        all_elem.append(start.val)
        start = start.next
    print(all_elem)

headA = createLinkedList([1,2,4])
headB = createLinkedList([1,3,4])
headC = mergeTwoLists(headA,headB)
printLinkedList(headC)