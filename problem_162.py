"""
    This solution:
    Passing tests mostly, bug exists, fix that!
"""

class Node:
    def __init__(self, key = 0, val=0, previous=None, next=None):
        self.key = key
        self.val = val
        self.previous = previous
        self.next = next


class LRUCache:

    """
        For LRU implementation
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hash_map = {}
        self.head = None
        self.tail = None

    
    def update_cache(self, node):
        if self.size == 1:
            return
        elif node == self.tail:
            return
        elif node == self.head:
            self.head = self.head.next
            self.head.previous = None
        else:
            if node.previous:
                node.previous.next = node.next
            if node.next:
                node.next.previous = node.previous
        
        node.previous = None
        node.next = None
        self.add_node(node)
        
    
    def add_node(self,node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
        
        self.size += 1
        
        
    def delete_node(self):
        if self.size == 1:
            del self.hash_map[self.head.key]
            self.head = None
            self.tail = None
            return
        else:
            del self.hash_map[self.head.key]
            self.head = self.head.next
            if self.head:
                self.head.previous = None
                
        self.size -= 1
                
    def display_lru(self):
        print('begining of list:')
        curr = self.head
        while curr:
            print(curr.val, end = '')   
            curr = curr.next
        print('end of list')
        #print(f'hash_map: {self.hash_map}')
    
        
    def get(self, key: int) -> int:
        #self.display_lru()
        node = self.hash_map.get(key)
        if not node:
            return -1
        else:
            self.update_cache(node)
            return node.val
        
        
    def put(self, key: int, value: int) -> None:
        node = self.hash_map.get(key)
        if node:
            self.hash_map[key].val = value
            self.update_cache(node)
        else:
            node2 = Node(key, value)
            if self.size >= self.capacity:
                self.delete_node()
            
            self.add_node(node2)
            self.hash_map[key] = node2
            
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)