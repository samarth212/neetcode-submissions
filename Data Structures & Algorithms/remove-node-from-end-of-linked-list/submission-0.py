# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        c = head
        listLen = 0
        while c:
            listLen +=1
            c = c.next

        indexToRemove = listLen - n

        c = dummy
        i = -1
        while c.next:

            if i + 1 == indexToRemove:
                c.next = c.next.next
                break
            i +=1
            c = c.next

        return dummy.next

        