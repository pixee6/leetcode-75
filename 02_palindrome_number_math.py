# LeetCode Problem: Palindrome Number (without string conversion)
# Check if a number is the same forward and backward using math only

def isPalindrome(x):
    if x < 0:
        return False

    original = x
    reversed_num = 0

    while x > 0:
        digit = x % 10                  # Get last digit
        reversed_num = reversed_num * 10 + digit  # Add digit to reversed number
        x = x // 10                     # Remove last digit

    return original == reversed_num     # Compare reversed with original

# Test cases
print(isPalindrome(121))   # True
print(isPalindrome(-121))  # False
print(isPalindrome(10))    # False
