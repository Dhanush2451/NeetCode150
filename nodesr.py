# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        i=head
        j=0
        while i and j <k:
            i=i.next
            j+=1
        if j==k:
            i=self.reverseKGroup(i,k)
            while j>0:
                temp=head.next
                head.next=i
                i=head
                head=temp
                j-=1
            head=i
        return head
