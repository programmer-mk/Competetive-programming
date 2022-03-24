# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        if not list1 and not list2:
            pass
            #print('Both lists empty')
        elif not list2:
            result = list1
        elif not list1:
            result = list2
        else:
            if list1.val <= list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                result =  list1
            else:
                list2.next =  self.mergeTwoLists(list1, list2.next)
                result = list2
            
        return result
        