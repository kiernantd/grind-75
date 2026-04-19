# Longest Palindromic Substring

## Problem
Given a string `s`, return the longest substring that reads the same forwards and backwards.

## Brute Force
Check every possible substring and test if it's a palindrome by comparing it to its reverse.

- Time: O(n³) — O(n²) substrings, O(n) palindrome check each
- Space: O(n) — storing the substring

## Optimized Approach
Expand around center. For each index, try expanding outward in both directions while the characters match. Handle both odd-length (single center) and even-length (two-character center) palindromes separately.

- Time: O(n²) — n centers, each expanding up to n steps
- Space: O(1) — just tracking indices (slicing at the end is O(n) but only once)

There's an O(n) algorithm (Manacher's), but expand-around-center is the sweet spot for interviews — clean, correct, and easy to explain.

## Reflection
The split between `expand(i, i)` for odd and `expand(i, i+1)` for even is easy to forget. Also worth noting the slice `s[left + 1 : right]` — after the while loop exits, `left` and `right` have gone one step too far in each direction, so we correct by `+1` and leaving `right` as-is (Python slicing is exclusive on the right).
