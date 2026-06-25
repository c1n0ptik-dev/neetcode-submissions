class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MinStack:

    def __init__(self):
        self.head = None
        self.stack = []

    def push(self, val: int) -> None:
        curr_min = val if not self.stack else min(val, self.stack[-1][-1])
        self.stack.append((val, curr_min))
        new_node = Node(val)
        new_node.next = self.head

        self.head = new_node

    def pop(self) -> None:
        self.stack.pop()
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.stack[-1][-1]

