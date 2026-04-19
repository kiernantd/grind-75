class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        max_length = 0

        for i, char in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1  # jump left past the duplicate
            seen[char] = i
            max_length = max(max_length, i - left + 1)
        return max_length