# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        list1 = head
        list2 = slow.next
        slow.next = None

        temp = None 
        prev = None
        curr = list2

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        curr = list1

        temp_list1 = None
        temp_prev = None

        while list1 and prev:
            temp_list1 = list1.next
            temp_prev = prev.next

            list1.next = prev
            list1 = temp_list1

            prev.next = list1
            prev = temp_prev
