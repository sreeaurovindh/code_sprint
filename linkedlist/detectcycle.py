class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return -1
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return -1
            slow = slow.next
            fast = fast.next.next

        start = head
        index = 0
        while start != fast:
            start = start.next
            fast = fast.next
            index = index + 1

        return index

t = Solution()
input = [3,2,0,-4]
cycle_point = 1

head = ListNode(input[0])
curr = head
loop_node = None
last_node  = None
for i in range(1,len(input)):
    temp = ListNode(input[i])
    if i == cycle_point:
        loop_node = temp
    if i == (len(input) -1):
        last_node = temp
    curr.next = temp
    curr = curr.next
last_node.next = loop_node

print(t.detectCycle(head))









