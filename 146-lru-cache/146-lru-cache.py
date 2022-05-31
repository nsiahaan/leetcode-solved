class Node:
    def __init__(self, key, value): # implement a doubly linked list to maintain pairs
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict() # map to nodes to achieve O(1) time
        self.head = Node(0, 0) # maintain a DLL, with node nearest head = most recently used (LRU at tail)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key].value
            self.removeNode(self.cache[key])
            self.insertNode(self.cache[key])
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value # update value
            self.removeNode(self.cache[key])
            self.insertNode(self.cache[key])
        else:
            node = Node(key, value)
            if len(self.cache) >= self.capacity:
                self.removeTail()
            self.cache[key] = node
            self.insertNode(node)
        
    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        
    def removeTail(self):
        if len(self.cache) == 0:
            return
        tail = self.tail.prev
        self.removeNode(tail)
        del self.cache[tail.key]
        
    def insertNode(self, node): # insert at head
        old_head = self.head.next
        self.head.next = node
        node.next = old_head
        old_head.prev = node
        node.prev = self.head
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)