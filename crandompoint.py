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
        copy={None:None}
        co=head
        while co:
            cop=Node(co.val)
            copy[co]=cop
            co=co.next
        co=head
        while co:
            cop=copy[co]
            cop.next=copy[co.next]
            cop.random=copy[co.random]
            co=co.next
        return copy[head]
