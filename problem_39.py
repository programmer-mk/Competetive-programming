# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    current_count = 0
    max_count = 0
    previous = None
    result = []

    def process(self, root: Optional[TreeNode]):
        if not self.previous:
            self.previous = root
            self.current_count = 1
            self.max_count = 1
            self.result = [self.previous.val]
        elif self.previous.val == root.val:
            self.current_count += 1
            if self.current_count == self.max_count:
                self.result.append(root.val)
            elif self.current_count > self.max_count:
                self.max_count = self.current_count
                self.result = [root.val]
        else:
            self.previous = root
            self.current_count = 1
            if self.current_count == self.max_count:
                self.result.append(root.val)
            elif self.current_count > self.max_count:
                self.max_count = self.current_count
                self.result = [root.val]


    def inorder(self, root: Optional[TreeNode]):
        if not root:
            return

        self.inorder(root.left)
        self.process(root)
        self.inorder(root.right)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.inorder(root)
        return self.result

