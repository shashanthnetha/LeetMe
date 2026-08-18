# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        total = 0

        head = head.next

        while head:

            if head.val == 0:
                current.next = ListNode(total)
                current = current.next
                total = 0
            else:
                total += head.val

            head = head.next

        return dummy.next
        