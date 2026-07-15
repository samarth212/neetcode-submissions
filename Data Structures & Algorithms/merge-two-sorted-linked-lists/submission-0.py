# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        new = dummy

        c1 = list1
        c2 = list2

        while c1 and c2:
            if c1.val <= c2.val:
                new.next = c1
                c1 = c1.next
                new = new.next
            else:
                new.next = c2
                c2 = c2.next
                new = new.next
        
        if c1:
            new.next = c1
        else:
            new.next = c2
        
        return dummy.next

        

        