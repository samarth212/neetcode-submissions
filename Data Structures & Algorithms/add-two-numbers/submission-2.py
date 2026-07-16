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

        while c1 or c2:
            v1 = c1.val if c1 else 0
            v2 = c2.val if c2 else 0
            if carry + v1 + v2 > 9:
                new.next = ListNode()
                new.next.val = (carry +v1+ v2)%10
                carry = 1
            else:
                carry = 0
                new.next = ListNode()
                new.next.val = v1+ v2

            new = new.next
            c1 = c1.next if c1 else None
            c2 = c2.next if c2 else None


        if not c1 and not c2 and carry:
            new.next = ListNode(1)
        elif c1 and not c2:
            new.next = c1
        elif c2 and not c1:
            new.next = c2

        return dummy.next
        