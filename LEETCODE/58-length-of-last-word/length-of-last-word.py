class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split() without arguments splits by any whitespace 
        # and discards empty strings.
        words = s.split()
        return len(words[-1])