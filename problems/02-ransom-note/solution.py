class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}

        if len(ransomNote) > len(magazine):
            return False
        
        # Build frequency map of magazine
        for letter in magazine:
            if letter in freq:
                freq[letter] += 1  # was freq[ransomNote]
            else:
                freq[letter] = 1   # was freq[ransomNote]
        
        # Check ransomNote against it
        for letter in ransomNote:  # loop over ransomNote, not freq
            if letter not in freq or freq[letter] == 0:  # "not in", not "is not in"
                return False
            freq[letter] -= 1  # use up one of that letter
        
        return True