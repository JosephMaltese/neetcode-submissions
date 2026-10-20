# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        current = head

        while current is not None:
            l+= 1
            current = current.next
        
        node_to_remove = l - n + 1

        current, prev = head, None
        currentNodeNum = 0
        
        while current is not None:
            currentNodeNum += 1

            if currentNodeNum == node_to_remove:
                if currentNodeNum != 1:
                    prev.next = current.next
                else:
                    head = current.next
                break
            prev = current
            current = current.next
        return head
        
        