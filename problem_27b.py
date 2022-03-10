# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue

class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # use modified level order algorithm
        nodes_queue = queue.Queue()
        nodes_queue.put(root.left)
        nodes_queue.put(root.right)
        while nodes_queue.qsize() > 0:
            left = nodes_queue.get()
            right = nodes_queue.get()

            if not left and not right:
                continue

            if not left or not right:
                return False

            if left.val != right.val:
                print('here')
                return False

            nodes_queue.put(left.left)
            nodes_queue.put(right.right)
            nodes_queue.put(left.right)
            nodes_queue.put(right.left)

        return True