class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        # For head
        while head is not None and head.val == val:
            head = head.next

        if head is None:
            return head

        # For the rest of elemens

        prev = None
        curr = head
        while curr is not None:
            if curr.val == val:
                if curr.next is not None:
                    temp = curr.next
                    prev.next = curr.next
                    curr = temp
                else:
                    prev.next = None
                    curr = curr.next
            else:
                prev = curr
                curr = curr.next


        return head


input = [1,2,6,3,4,5,6]
head = ListNode(input[0])
curr = head

for i in range(1,len(input)):
    temp = ListNode(input[i])
    curr.next = temp
    curr = curr.next

t = Solution()
t.removeElements(head,6)

