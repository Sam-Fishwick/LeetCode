# Given the head of a singly linked list, reverse the list, and return the 
# reversed list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        head = prev
        return head
