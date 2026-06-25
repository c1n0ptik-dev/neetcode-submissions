class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next  

class LRUCache:

    def __init__(self, capacity: int):
       self.capacity = capacity
       self.hashmap = {}

       self.head = Node()
       self.tail = Node()

       self.head.next = self.tail
       self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        temp = self.head.next

        self.head.next = node
        node.next = temp
        node.prev = self.head
        temp.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1
       
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.remove(node)
            self.add(node)

        else:
            if len(self.hashmap) >= self.capacity:
                removeNode = self.tail.prev
                self.remove(removeNode)
                del self.hashmap[removeNode.key]
            
            newNode = Node(key, value)
            self.hashmap[key] = newNode
            self.add(newNode)
        

        
            
        
        
