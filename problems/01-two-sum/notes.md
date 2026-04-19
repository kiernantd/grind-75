# Two Sum

## Problem
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`. Each input has exactly one solution and you may not use the same element twice.

## Brute Force
Check every pair of elements with a nested loop. For each element at index `i`, scan every element after it to see if they sum to `target`.

- Time: O(n²) — two nested loops
- Space: O(1)

## Optimized Approach
Use a hash map to store each number and its index as we iterate. For each new number, check if its complement (`target - num`) is already in the map — if so, we found our pair.

- Time: O(n) — single pass
- Space: O(n) — hash map stores up to n elements

The key insight: instead of searching forward for the complement, we look backward into what we've already seen.

## Reflection
This is the classic intro to trading space for time. The hash map turns an O(n) search into O(1) lookup. Worth remembering that we store `value → index` (not index → value) since we look up by value and need to return the index.
