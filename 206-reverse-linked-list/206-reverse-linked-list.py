# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        nhead = head
        ptr = head.next
        nhead.next = None # remove cycle
        
        while (ptr):
            temp = ptr.next
            ptr.next = nhead
            nhead = ptr
            ptr = temp
            
        return nhead