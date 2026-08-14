# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        # If removing the first node
        if n == length:
            return head.next

        # Move to node before the one to remove
        current = head

        for i in range(length - n - 1):
            current = current.next

        # Remove the node
        current.next = current.next.next

        return head