import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        i = 0

        head = ListNode()
        dummy = head

        for node in lists:
            i += 1
            heapq.heappush(h, (node.val, i, node))     

        while h:
            val, i, node = heapq.heappop(h)

            dummy.next = node
            dummy = dummy.next

            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))
                i += 1

        return head.next