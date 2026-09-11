# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast is not None:
            if fast.next == slow:
                return True
            slow = slow.next
            fast = fast.next
            if fast is None:
                return False
            fast = fast.next
        return False
