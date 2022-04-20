# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    """
        Approach:
            - keep two pointers: slow and fast. Slow move one step, fast two steps.Middle node will be on slow pointer.
              Time complexity: O(n), Space complexity O(1)
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next
            fast = fast.next
            slow = slow.next
            
        return slow
        