from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = deque()
  # TODO: Write your code here
  if not root:
    return result

  queue = deque()
  queue.append(root)
  while len(queue) > 0:
    level_size = len(queue)
    level_nodes = []
    for _ in range(level_size):
      current = queue.popleft()
      level_nodes.append(current.val)
      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)
    result.appendleft(level_nodes)
  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(traverse(root)))


main()
