# Word Break

## Problem
Given a string `s` and a list of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

## Brute Force
Recursively try every possible prefix of `s` — if it's in the dictionary, recurse on the remainder. Exponential time without memoization due to overlapping subproblems.

## Optimized Approach
Bottom-up DP. `dp[i]` means the first `i` characters of `s` can be segmented using words in the dictionary.

- Base case: `dp[0] = True` (empty string is always valid)
- For each position `i` where `dp[i]` is true, try extending by every word in the dictionary: if `s[i:i+len(word)] == word`, mark `dp[i+len(word)] = True`
- Answer is `dp[len(s)]`

- Time: O(n * m * k) — n positions, m words, k max word length for the slice comparison
- Space: O(n)

## Reflection
The key insight is that `dp[0] = True` seeds the whole computation — without it nothing propagates. The loop only does work at positions already marked true, so it naturally skips dead ends. Watch out for the off-by-one: the dp array is length `n+1` and the final answer is at index `n`, not `n-1`.
