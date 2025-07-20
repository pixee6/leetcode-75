# LeetCode Problem: Roman to Integer
# Convert a Roman numeral string to an integer using a dictionary and reverse loop

class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to map Roman symbols to their values
        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0   # This will store the final result
        prev = 0    # This keeps track of the previous value during the loop

        # Loop through the string in reverse (right to left)
        for ch in reversed(s):
            curr = roman[ch]  # Get the integer value of the current Roman character

            if curr < prev:
                # If current value is smaller than the previous one,
                # subtract it (like in IV = 5 - 1 = 4)
                total -= curr
            else:
                # Otherwise, add the value normally
                total += curr

            # Update previous value for the next loop
            prev = curr

        # Return the final calculated integer
        return total


# Create an object of the class to call the method
solution = Solution()

# Test cases
print(solution.romanToInt("III"))      # Output: 3
print(solution.romanToInt("LVIII"))    # Output: 58
print(solution.romanToInt("MCMXCIV"))  # Output: 1994
