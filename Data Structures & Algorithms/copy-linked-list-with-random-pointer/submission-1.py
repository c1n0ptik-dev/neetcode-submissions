"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        nodes = {}
        dummy = Node(x = 0, next = head)

        while head:
            new_node = Node(x = head.val, random = None, next = None)
            nodes[head] = new_node
            head = head.next

        dummy = dummy.next

        new_head = nodes[dummy]
        new_dummy = Node(x = 0, next = new_head)

        while dummy: 
            new_head = nodes[dummy]
            if dummy.next == None:
                new_head.next = None
            else:
                new_head.next = nodes[dummy.next]
            if dummy.random == None:
                new_head.random = None
            else:
                new_head.random = nodes[dummy.random]

            new_head = new_head.next
            dummy = dummy.next
        
        return new_dummy.next
        


        

            

