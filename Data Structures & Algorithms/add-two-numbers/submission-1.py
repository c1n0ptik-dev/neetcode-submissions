# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = int(self.extract_number(l1))
        n2 = int(self.extract_number(l2))

        n3 = n1 + n2
        result = list((str(n3)[::-1]))

        head = ListNode(int(result[0]))
        curr = head

        for i in result[1:]:
            curr.next = ListNode(int(i))
            curr = curr.next

        return head

    def extract_number(self, head):
        temp = None
        prev = None
        number = ""

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        while prev:
            number += str(prev.val)
            prev = prev.next
        
        return number
