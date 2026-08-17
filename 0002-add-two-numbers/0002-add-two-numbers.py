# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        values1 = []
        values2 = []

        while l1:
            values1.append(l1.val)
            l1 = l1.next

        while l2:
            values2.append(l2.val)
            l2 = l2.next

        a = int("".join(map(str, values1[::-1])))
        b = int("".join(map(str, values2[::-1])))

        c = a + b

        result = list(map(int, str(c)[::-1]))

        dummy = ListNode(0)
        current = dummy

        for i in result:
            current.next = ListNode(i)
            current = current.next

        return dummy.next
                