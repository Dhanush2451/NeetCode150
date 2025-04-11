# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s=set()
        co=head
        while co:
            if co in s:
                return True
            s.add(co)
            co=co.next
        return False
