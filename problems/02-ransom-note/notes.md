# Ransom Note

## Problem
Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed using letters from `magazine`. Each letter in `magazine` can only be used once.

## Brute Force
For each character in `ransomNote`, scan through `magazine` to find a match, and mark it used. This requires modifying the magazine string or tracking used indices separately.

- Time: O(n * m) — for each of n ransom chars, scan up to m magazine chars
- Space: O(1) or O(m) depending on implementation

## Optimized Approach
Build a frequency map of `magazine` characters first, then for each character in `ransomNote`, decrement its count. If a character is missing or depleted, return `False`.

- Time: O(n + m) — one pass over each string
- Space: O(1) — at most 26 lowercase letters in the map

## Reflection
Another frequency map pattern — very similar to Two Sum in spirit. The early-exit check (`len(ransomNote) > len(magazine)`) is a nice cheap guard. A common mistake here is accidentally building the map from `ransomNote` instead of `magazine` — the map needs to represent what's *available*.
