# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values=[]
        while head:
            values.append(head.val)
            head = head.next
        result = []
        

        for x in values:
            if values.count(x) == 1:
                result.append(x)

        dummy = ListNode(0)
        current = dummy

        for x in result:
            current.next = ListNode(x)
            current = current.next

        return dummy.next
        