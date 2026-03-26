class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        h_len = len(haystack)
        n_len = len(needle)
        
        # Only need to loop up to the point where needle can still fit
        for i in range(h_len - n_len + 1):
            # Check if the substring matches
            if haystack[i : i + n_len] == needle:
                return i
                
        return -1