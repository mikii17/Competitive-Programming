# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pter1 = head
        pter2 = head
        
        while pter2.next and pter2.next.next:
            pter1 = pter1.next
            pter2 = pter2.next.next
        
        if pter2.next:
            return pter1.next
        return pter1