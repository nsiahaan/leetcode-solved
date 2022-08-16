# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use slow and fast pointer, if slow reaches end w/o matching fast, no cycle
        slow, fast = head, head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False