# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        firstPointer = head

        while firstPointer.next != None and firstPointer.next.next != None:
            secondPointer = firstPointer
            prev = None

            while secondPointer.next != None:
                prev = secondPointer
                secondPointer = secondPointer.next
            prev.next = None

            nextPointer = firstPointer.next
            firstPointer.next = secondPointer
            secondPointer.next = nextPointer
            firstPointer = firstPointer.next.next