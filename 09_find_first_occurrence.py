class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            # Take a piece of haystack same length as needle
            if haystack[i : i + len(needle)] == needle:
                # If it matches, return the starting index
                return i
        # If not found, return -1
        return -1
      
