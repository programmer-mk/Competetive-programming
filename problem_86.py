class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers_recursive(root, sum):
  if not root:
    return 0

  temp_sum = sum + root.val
  left = find_sum_of_path_numbers_recursive(root.left, temp_sum * 10)
  right = find_sum_of_path_numbers_recursive(root.right, temp_sum * 10)
  return max(left + right, temp_sum)


def find_sum_of_path_numbers(root):
  if not root:
    return 0

  return find_sum_of_path_numbers_recursive(root, 0)


def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
