# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        #                     
        # [[1,2,4],[1,3,5],[3,6]]
        # 

        # curMin = 6
        # minPointer = 2


        # [1, 1, 2, 3, 3, 4, 5, 6]
        
        dummy = ListNode()
        new = dummy
        k = len(lists)
        pointers = {}
        null = {}

        for i in range(k):
            pointers[i] = lists[i]
            null[i] = None

        while pointers != null:
            curMin = 1001
            minPointer = -1
            for i in range(k):
                if pointers[i] and pointers[i].val < curMin:
                    curMin = pointers[i].val
                    minPointer = i
            new.next = pointers[minPointer]
            new = new.next
            pointers[minPointer] = pointers[minPointer].next

        return dummy.next
            
            






        