# Longest Substring Without Repeating Characters

## Problem
Given a string `s`, find the length of the longest substring that contains no repeating characters.

## Brute Force
Generate all possible substrings, check each one for duplicates using a set, and track the maximum length found.

- Time: O(n³) — O(n²) substrings, each taking O(n) to check
- Space: O(n) — for the set

## Optimized Approach
Sliding window with a hash map. Maintain a `left` pointer and expand `right` across the string. When a duplicate is found, jump `left` past the previous occurrence of that character (using the stored index) rather than moving one step at a time.

- Time: O(n) — each character is visited at most twice
- Space: O(n) — hash map of character positions

The jump `left = seen[char] + 1` is the key move — it skips directly to a valid window instead of shrinking one character at a time.

## Reflection
This is the sliding window pattern at its most elegant. The subtle part is the guard `seen[char] >= left` — without it, you'd incorrectly shrink the window based on a character occurrence that's already outside the current window. The window only ever grows or stays the same size, which is why we can track `max_length` incrementally.
