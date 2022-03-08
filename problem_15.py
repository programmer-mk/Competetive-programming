# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def helper(self, root: Optional[TreeNode], min: int, max: int) -> bool:
        if not root:
            return True
        if root.val <= min or root.val >= max:
            return False

        return self.helper(root.left, min, root.val) and self.helper(root.right, root.val, max)


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root,-2**31-1, 2**31)