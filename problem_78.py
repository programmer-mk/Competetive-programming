"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
            
        queue = deque()
        queue.append(root)
        while len(queue):
            N = len(queue)
            previous = None
            #print([elem.val for elem in queue])
            for idx in range(N):
                current_node = queue.popleft()
                if previous:
                    previous.next = current_node
                    previous = current_node
                else:
                    previous = current_node
                if idx == N-1:
                    current_node.next = None
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
        return root
        