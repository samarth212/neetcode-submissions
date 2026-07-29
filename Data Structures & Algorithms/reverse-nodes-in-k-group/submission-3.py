class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        s = dummy

        while True:
            K = s

            for _ in range(k):
                K = K.next
                if not K:
                    return dummy.next

            groupNext = K.next
            c = s.next
            p = groupNext

            while c != groupNext:
                n = c.next
                c.next = p
                p = c
                c = n

            s.next, s = K, s.next