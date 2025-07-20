# LeetCode Problem: Two Sum
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# Each input has exactly one solution, and you may not use the same element twice.

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Test case
print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
