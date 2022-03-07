# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        slow = head
        fast = head
        for i in range(0, n):
            if fast.next is None:
                if i == n - 1:
                    head = head.next
                return head
            fast = fast.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        if slow.next is not None:
            slow.next = slow.next.next
        return head