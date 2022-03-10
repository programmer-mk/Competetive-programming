# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSymmetricHelper(self, left: Optional[TreeNode], right: Optional[TreeNode]):
        if not left or not right:
            return left == right
        elif left.val != right.val:
            print(f'vals: {left.val}, {right.val}')
            return False
        else:
            return self.isSymmetricHelper(left.left, right.right) and self.isSymmetricHelper(left.right,right.left)


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        else:
            return self.isSymmetricHelper(root.left, root.right)

