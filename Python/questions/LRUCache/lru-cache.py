class Node:
    def __init__(self, key: int, value: int, prev: 'Node' = None, next: 'Node' = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.hashset = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        
    def add(self, newNode: 'Node'):
        oldHead = self.head.next
        self.head.next = newNode
        newNode.next = oldHead
        oldHead.prev = newNode
        newNode.prev = self.head
        
    def remove(self, node: 'Node'):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key: int) -> int:
        if key in self.hashset:
            node = self.hashset[key]
            self.remove(node)
            self.add(node)
            return node.value
        
        return -1

    def put(self, key: int, value: int) -> None:
        newNode = Node(key, value)
        
        if key in self.hashset:
            self.remove(self.hashset[key])
        elif len(self.hashset) >= self.capacity:
            del self.hashset[self.tail.prev.key]
            self.remove(self.tail.prev)

        self.add(newNode)
        self.hashset[key] = newNode
