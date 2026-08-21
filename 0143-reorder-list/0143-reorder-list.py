# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        values = []

        current = head

        # Store linked list values
        while current:
            values.append(current.val)
            current = current.next

        # Split into two halves
        mid = (len(values) + 1) // 2

        first = values[:mid]
        second = values[mid:][::-1]

        # Reorder
        result = []

        for i in range(len(second)):
            result.append(first[i])
            result.append(second[i])

        # If first half has one extra element
        if len(first) > len(second):
            result.append(first[-1])

        # Put values back into linked list
        current = head

        for value in result:
            current.val = value
            current = current.next