# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # d=ListNode(0)
        # d.next=head
        # current=d
        # while current.next:
        #     if current.next.val==val:
        #         current.next=current.next.next
        #     else:
        #         current=current.next
        # return d.next
        values=[]
        current=head
        while current:
            if current.val != val:
                values.append(current.val)
            current=current.next
        d=ListNode()
        current=d
        for i in values:
            current.next=ListNode(i)
            current=current.next
        return d.next