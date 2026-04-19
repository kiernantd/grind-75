class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        sign = 1
        i = 0
        
        # Stage 1: strip leading whitespace
        s = s.lstrip()
        
        # guard against empty string
        if not s:
            return 0
        
        # Stage 2: check for sign
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1
        
        # Stage 3: build number digit by digit
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        # Stage 4: apply sign and clamp
        result *= sign
        result = max(-2**31, min(result, 2**31 - 1))
        
        return result