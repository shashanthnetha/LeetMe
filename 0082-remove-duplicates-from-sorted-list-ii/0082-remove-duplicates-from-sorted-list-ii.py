# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values=[]
        current=head
        while current:
            values.append(current.val)
            current=current.next
        result=[]
        for i in values:
            if values.count(i)==1:
                result.append(i)
        d=ListNode()
        current=d
        for i in result:
            current.next=ListNode(i)
            current=current.next
        return d.next