# 11. Container With Most Water

**Difficulty:** Medium
**Topic:** Two Pointers
**Link:** https://leetcode.com/problems/container-with-most-water/

---

## Problem

Given an array `heights` where `heights[i]` is the height of a vertical line at index `i`, find two lines that together with the x-axis form a container that holds the most water. Return the maximum amount of water.

---

## Brute Force — O(n²) time, O(1) space

Try every pair `(i, j)`. Area = `min(heights[i], heights[j]) * (j - i)`.

```python
res = 0
for i in range(len(heights)):
    for j in range(i + 1, len(heights)):
        res = max(res, min(heights[i], heights[j]) * (j - i))
return res
```

**My submitted solution.** Correct but slow for large inputs.

---

## Optimized — Two Pointers — O(n) time, O(1) space

Start with the widest possible container (`l=0`, `r=n-1`). The area is limited by the shorter wall, so moving the pointer at the taller wall inward can never increase the area — only moving the shorter one can. Greedily move whichever pointer points to the shorter wall.

```python
l, r = 0, len(heights) - 1
res = 0
while l < r:
    res = max(res, min(heights[l], heights[r]) * (r - l))
    if heights[l] < heights[r]:
        l += 1
    else:
        r -= 1
return res
```

---

## Key Insight

Width shrinks by 1 each step regardless. The only chance to find a bigger area is a taller wall, so always discard the shorter side.

---

## Complexity

| | Brute Force | Two Pointers |
|-|-------------|--------------|
| Time | O(n²) | O(n) |
| Space | O(1) | O(1) |
