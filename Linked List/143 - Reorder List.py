# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        pre = None

        while slow:
            nxt = slow.next
            slow.next = pre
            pre = slow
            slow = nxt

        while pre.next:
            tmp = head.next
            head.next = pre
            head = tmp

            tmp = pre.next
            pre.next = head
            pre = tmp
