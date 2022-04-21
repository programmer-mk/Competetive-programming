# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            root = None
        elif root1 is None:
            root = TreeNode(root2.val)
            root.left = self.mergeTrees(None, root2.left)
            root.right = self.mergeTrees(None, root2.right)
        elif root2 is None:
            root = TreeNode(root1.val)
            root.left = self.mergeTrees(root1.left, None)
            root.right = self.mergeTrees(root1.right, None)
        else:
            root = TreeNode(root1.val+root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
            
        return root