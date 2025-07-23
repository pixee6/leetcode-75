class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "]":"[", "}":"{"}

        for char in s:
            if char in mapping.values():  # opening bracket
                stack.append(char)
            elif char in mapping:  # closing bracket
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                return False 

        return len(stack) == 0  

# Test cases
sol = Solution()
print(sol.isValid("()"))        # True
print(sol.isValid("()[]{}"))    # True
print(sol.isValid("(]"))        # False
print(sol.isValid("([])"))      # True
print(sol.isValid("([)]"))      # False
