class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True

          




    def simpleReverse(self,head):
        slow = head
        prev = None
        while slow is not None:
            node = slow
            slow = slow.next
            node.next = prev
            prev = node
        self.printLinkedList(prev)


    def printLinkedList(self,head):
        all_elem = []
        start = head
        while start is not None:
            all_elem.append(start.val)
            start = start.next
        print(all_elem)




input = [1,2,3,2,1]
head = ListNode(input[0])
curr = head

for i in range(1,len(input)):
    temp = ListNode(input[i])
    curr.next = temp
    curr = curr.next

t = Solution()
print(t.isPalindrome(head))
#t.simpleReverse(head)