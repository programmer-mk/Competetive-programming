from __future__ import print_function
from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next


def connect_all_siblings(root):
  if not root:
    return None

  queue = deque()
  queue.append(root)
  previous_level_tail = None
  previous = None
  while len(queue):
    N = len(queue)
    for i in range(N):
      node = queue.popleft()
      if not previous:
        previous = node
      else:
        previous.next = node
        previous = node

      if not previous_level_tail:
        previous_level_tail = node
      elif previous_level_tail and i == 0:
        previous_level_tail.next = node
      elif previous_level_tail and i == N-1:
        previous_level_tail = node
      
      if node.left:
        queue.append(node.left)

      if node.right:
        queue.append(node.right)
    previous = None
  

  return


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_all_siblings(root)
  root.print_tree()


main()
