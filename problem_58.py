# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = []
    
    def pathSumHelper(self, root: Optional[TreeNode], targetSum: int, current_path):
        if not root:
            return
        current_path.append(root.val)
        
        if not root.left and not root.right and root.val == targetSum:
            self.result.append(current_path.copy())
            return
            
        self.pathSumHelper(root.left, targetSum - root.val, current_path.copy())
        self.pathSumHelper(root.right, targetSum - root.val, current_path.copy())
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        self.pathSumHelper(root, targetSum, [])
        return self.result
        