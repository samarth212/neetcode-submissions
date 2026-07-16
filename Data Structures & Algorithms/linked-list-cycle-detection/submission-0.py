# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # have a slow and fast pointer
        # if at any point the slow == fast, we have a cycle
        # if at any point the fast == null, not a cycle

        slow = fast = head

        while slow.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            elif not fast:
                return False

        return False



        



        