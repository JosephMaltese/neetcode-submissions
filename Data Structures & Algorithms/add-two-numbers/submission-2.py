# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        res = ListNode()
        currentNode = res
        carryOver = 0
        while l1 is not None or l2 is not None:
            firstVal = 0 if l1 is None else l1.val
            secondVal = 0 if l2 is None else l2.val
            totalSum = firstVal + secondVal + carryOver
            remainder = totalSum % 10
            carryOver = totalSum // 10
            currentNode.val = remainder
            l1 = l1 if l1 is None else l1.next
            l2 = l2 if l2 is None else l2.next
            if l1 is not None or l2 is not None or carryOver != 0:
                nextNode = ListNode()
                currentNode.next = nextNode
                currentNode = nextNode
        if carryOver != 0:
            currentNode.val = carryOver
        return res

        