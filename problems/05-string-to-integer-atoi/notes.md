# String to Integer (atoi)

## Problem
Implement `myAtoi(s)` which converts a string to a 32-bit signed integer. The function must handle leading whitespace, an optional sign (`+` or `-`), digit parsing, non-digit termination, and clamping to `[-2³¹, 2³¹ - 1]`.

## Brute Force
There isn't really a "brute force" here — this is a pure parsing problem. A naive approach might use Python's built-in `int()` with a try/except, but that doesn't handle the specific edge cases the problem requires (non-digit termination, clamping).

## Optimized Approach
Process the string in four explicit stages:
1. Strip leading whitespace with `lstrip()`
2. Read optional sign character
3. Consume digits one by one, building the integer
4. Apply sign and clamp to 32-bit bounds

- Time: O(n) — single pass
- Space: O(1)

The `while s[i].isdigit()` loop naturally terminates on any non-digit character, handling that edge case for free.

## Reflection
This problem is less about algorithms and more about careful state management. The easy mistakes are: forgetting the empty string guard after `lstrip()`, not handling `+` sign (only handling `-`), and forgetting to apply `sign` before clamping. The clamping line `max(-2**31, min(result, 2**31 - 1))` is a clean Python idiom worth memorizing.
