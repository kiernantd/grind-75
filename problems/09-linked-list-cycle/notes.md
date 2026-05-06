# Linked List Cycle

## Problem
Given the `head` of a linked list, determine if the list has a cycle in it.

## Brute Force
Track every visited node in a hash set. If you encounter a node already in the set, there's a cycle. O(n) time and O(n) space.

## Optimized Approach
Floyd's Cycle Detection (tortoise and hare). Use two pointers: `slow` moves one step at a time, `fast` moves two. If there's a cycle, fast will eventually lap slow and they'll meet. If there's no cycle, fast will hit `None`.

- Initialize `slow = head`, `fast = head.next` (offset so the while condition `slow != fast` doesn't exit immediately)
- Loop while `fast` and `fast.next` are not `None` and `slow != fast`
- If they meet, there's a cycle; if the loop exits without meeting, no cycle

- Time: O(n)
- Space: O(1)

## Reflection
Key insight behind Floyd's: in a cycle, the fast pointer gains one step on slow per iteration, so it's guaranteed to lap it rather than skip over it. Remember the empty list edge case (`head is None`) — this is an easy one to miss on the first attempt.
