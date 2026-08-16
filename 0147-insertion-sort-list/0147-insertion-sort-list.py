# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []

        while head:
            values.append(head.val)
            head = head.next

        values.sort()

        dummy = ListNode(0)
        current = dummy

        for x in values:
            current.next = ListNode(x)
            current = current.next

        return dummy.next