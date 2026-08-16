# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values=[]
        while head:
            values.append(head.val)
            head=head.next
        values.sort()
        d=ListNode(0)
        current=d
        for x in values:
            current.next=ListNode(x)
            current=current.next
        return d.next

        