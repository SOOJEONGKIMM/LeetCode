# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = ListNode(None)
        node.next = head
        head = node
        while head.next:
            if head.next.val==val:
                head.next=head.next.next
            else:
                head = head.next
        return node.next
    