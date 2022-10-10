# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        ptr1 = head
        ptr2 = head.next.next
        isHeadDup = head.val == head.next.val
        isDup = False
    
        while ptr2:
            if ptr1.next.val != ptr2.val:
                if not isDup:
                    ptr1 = ptr1.next
                    ptr2 = ptr2.next
                else:
                    ptr1.next = ptr2
                    ptr2 = ptr2.next
                    isDup = False
            else:
                isDup = True
                ptr2 = ptr2.next
                
        if isDup:
            ptr1.next = None
        if isHeadDup:
            if head.next and head.val == head.next.val:
                return head.next.next
            return head.next
        return head
            