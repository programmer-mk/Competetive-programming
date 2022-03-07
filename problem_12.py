# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse_list(self, head):
        if head is None:
            return head

        previous = None
        current = head
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next

        return previous

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True

        slow = head
        fast = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            if fast is not None:
                slow = slow.next

        second_part = slow.next
        slow.next = None
        reversed = self.reverse_list(second_part)
        current = head
        while current != None and reversed != None:
            if current.val != reversed.val:
                return False
            current = current.next
            reversed = reversed.next

        if current != None and reversed != None:
            return False
        else:
            return True