# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing
# together the nodes of the first two lists.

# Return the head of the merged linked list.


# Allow Optional typing
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2

        merged: Optional[ListNode] = ListNode(0, None)
        prev: Optional[ListNode] = merged

        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                prev = list1
                list1 = list1.next
            else:
                prev.next = list2
                prev = list2
                list2 = list2.next

        prev.next = list1 if list1 else list2

        return merged.next
