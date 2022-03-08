# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        node_queue = queue.Queue()
        node_queue.put(root)
        result = []
        while not node_queue.empty():
            level = []
            level_size = node_queue.qsize()
            for i in range(level_size):
                target_node = node_queue.get()
                level.append(target_node.val)
                if target_node.left:
                    node_queue.put(target_node.left)
                if target_node.right:
                    node_queue.put(target_node.right)
            result.append(level)

        return result