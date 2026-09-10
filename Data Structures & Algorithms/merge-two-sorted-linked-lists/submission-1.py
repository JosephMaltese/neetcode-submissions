# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        res = ListNode()
        current = res

        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    current.val = list1.val
                    list1 = list1.next
                else:
                    current.val = list2.val
                    list2 = list2.next
            elif list1:
                current.val = list1.val
                list1 = list1.next
            else:
                current.val = list2.val
                list2 = list2.next
            if list1 or list2:
                nextNode = ListNode()
                current.next = nextNode
                current = current.next
        return res

                    

        