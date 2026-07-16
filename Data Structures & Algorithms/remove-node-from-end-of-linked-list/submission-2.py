# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        c1 = c2 = dummy

        for _ in range(n):
            c1 = c1.next
        
        while c1 and c1.next:
            c1 = c1.next
            c2 = c2.next
        
      
        c2.next = c2.next.next


        return dummy.next

        
        


        
            

        