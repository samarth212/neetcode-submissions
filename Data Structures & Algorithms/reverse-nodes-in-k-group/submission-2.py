# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        '''
        loop until the end
        count # iterations
        end, nextStart


        p, c, n

        if p is null, c.next -> end, contunue (head edge case)
            then, update pointers, and
            for the range of k-1 , reverse
            n = c.next
            c.next -> p
            p = c
            c = n

            head is now = p

        else,

        if c == end, advacne end, and point c.next -> end
        for the range of k , reverse
            n = c.next
            c.next -> p
            p = c
            c = n

        for every multiple of k iterations, advance end
            when we do this, keep track of its own counter; if the loop ends
            (end == null) and counter < k, do not reverse, and return 
        '''

        if not head.next:
            return head

        count = 0
        end = head
        
        # place starting end pointer
        while end and count < k:
            end = end.next
            count += 1
        if not end and count < k:
            return head
        
        # first k group
        p = None
        c = start = head
        n = head.next
        if not p:
            c.next = end
            p = c
            c = n
            n = c.next
            for _ in range(k-1):
                c.next = p
                p = c
                c = n
                if c:
                    n = c.next
                else:
                    return p
               
            head = p
            p = start
            start = c

        # for rest of nodes

        prevEnd = None

        while c:
            
            if c == end:
                if not prevEnd:
                    prevEnd = p
                count = 0
                while end and count < k:
                    end = end.next
                    count += 1
                if not end and count < k:
                    return head

                n = c.next
                c.next = end
                p = c
                c = n

            else:
                if c.next == end:
                    prevEnd.next = c
                n = c.next
                c.next = p
                p = c
                c = n
                


        return head
            

            

            






        

        

        
        



        
        