from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            letter = strs[0][i]  # Get current letter from the first word

            for word in strs:
                if i >= len(word) or word[i] != letter:
                    return prefix  # If mismatch, return prefix

            prefix += letter  # Only add letter if all words matched

        return prefix

# Create object of the class
sol = Solution()

# Call the function and print results
print(sol.longestCommonPrefix(["flower", "flow", "flight"])) 
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))
