# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        c1, c2 = l1, l2
        dummy = ListNode()
        new = dummy

        while c1 and c2:
            if carry + c1.val + c2.val > 9:
                new.next = ListNode()
                new.next.val = (carry + c1.val + c2.val)%10
                carry = 1
            else:
                carry = 0
                new.next = ListNode()
                new.next.val = c1.val + c2.val

            new = new.next
            c1 = c1.next
            c2 = c2.next


        if not c1 and not c2 and carry:
            new.next = ListNode(1)
        elif c1 and not c2:
            new.next = c1
        elif c2 and not c1:
            new.next = c2

        return dummy.next
        