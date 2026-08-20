"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}

        # 1. Create all new nodes
        curr = head

        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # 2. Connect next and random
        curr = head

        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next

        # 3. Return copied head
        return old_to_new.get(head)
        