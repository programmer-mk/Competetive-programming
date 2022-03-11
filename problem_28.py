# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if not l1 and not l2:
            return None

        previous = None
        current1 = l1
        current2 = l2
        increase = False
        first_pass = True
        head = None

        while current1 and current2:
            if increase:
                sum = current1.val + current2.val + 1
            else:
                sum = current1.val + current2.val
            if sum >= 10:
                increase = True
            else:
                increase = False

            new_node = ListNode(sum % 10)
            if first_pass:
                head = new_node
                first_pass = False

            if previous:
                previous.next = new_node

            previous = new_node
            current1 = current1.next
            current2 = current2.next

        while current1:
            if increase:
                sum = current1.val + 1
            else:
                sum = current1.val
            if sum >= 10:
                increase = True
            else:
                increase = False

            new_node = ListNode(sum % 10)
            if first_pass:
                head = new_node
                first_pass = False

            if previous:
                previous.next = new_node

            previous = new_node
            current1 = current1.next

        while current2:
            if increase:
                sum = current2.val + 1
            else:
                sum = current2.val
            if sum >= 10:
                increase = True
            else:
                increase = False

            new_node = ListNode(sum % 10)
            if first_pass:
                head = new_node
                first_pass = False

            if previous:
                previous.next = new_node

            previous = new_node
            current2 = current2.next


        if previous and increase:
            previous.next = ListNode(1)

        return head



