# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        values=[]
        while head:
            values.append(head.val)
            head=head.next
        a=[]
        b=[]
        for i in values:
            if i<x:
                a.append(i)
            else:
                b.append(i)
        values=a+b
        d=ListNode(0)
        current=d
        for i in values:
            current.next=ListNode(i)
            current=current.next
        return d.next
            

        
        