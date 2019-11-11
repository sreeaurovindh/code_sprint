class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def insertAtIndex(self,index,val):
        if index < 0 or index > self.size:
            return

        self.size = self.size + 1
        pred = self.head
        for _ in range(index):
            pred = pred.next

        to_add = ListNode(val)
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self,index):
        if index <0  or index > self.size:
            return

        pred = self.head
        for _ in range(index):
            pred = pred.next

        pred.next = pred.next.next
        self.size -= 1

        
