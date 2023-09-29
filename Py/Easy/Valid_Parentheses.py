# Given a string s containing just the characters '(', ')', '{', '}', '['
# and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        hash_map = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in ')]}':
                if not stack or stack.pop() != hash_map.get(char):
                    return False
            else:
                stack.append(char)
        return not stack
