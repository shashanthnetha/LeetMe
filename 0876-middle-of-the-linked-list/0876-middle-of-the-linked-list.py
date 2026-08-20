# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        current = head

        while current:
            values.append(current.val)
            current = current.next

        a = len(values)//2

        d = ListNode()
        current = d

        for i in values[a:]:
            current.next = ListNode(i)
            current = current.next

        return d.next
        