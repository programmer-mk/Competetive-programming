# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def merge(self, head1, head2):
        dummy_head = ListNode()
        tail = dummy_head
        while head1 and head2:
            if head1.val <= head2.val:
                tail.next = head1
                head1 = head1.next
                tail = tail.next
            else:
                tail.next = head2
                head2 = head2.next
                tail = tail.next
                    
        if head1:
            tail.next = head1
        else:
            tail.next = head2
        return dummy_head.next
    
    
    def get_middle(self, head: Optional[ListNode]):
        slow = None
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            if not slow:
                slow = head
            else:
                slow = slow.next
        mid = slow.next
        slow.next = None
        return mid
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        mid = self.get_middle(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
        
        