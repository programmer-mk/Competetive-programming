class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path_recursive(root, sequence, index):
  if index >= len(sequence) or not root:
    return False

  if sequence[index] != root.val:
    return False

  if index == len(sequence) - 1 and not root.left and not root.right:
    return True

  return find_path_recursive(root.left, sequence, index + 1) \
        or find_path_recursive(root.right, sequence, index + 1)


def find_path(root, sequence):
  if not root and not len(sequence):
    return True
  elif not root:
    return False
  else:
    return find_path_recursive(root, sequence, 0) 


def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
