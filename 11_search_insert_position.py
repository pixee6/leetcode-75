class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
      left= 0 
      right = nums -1
      while left <= target:
        #we found mid by adding left and right and dividing by 2
        mid= (left + right)//2
        # if the middle number is exactly the target, I found it
        if nums[mid] == target:
            return mid

        # if the middle number is smaller than target,
        # that means the target must be on the right side
        elif nums[mid] < target:
            left = mid + 1   # so I move my left pointer one step right

        # if the middle number is bigger than target,
        # that means the target must be on the left side
        else:
            right = mid - 1  # so I move my right pointer one step left

    # if I come out of the loop, that means target not found
    # now my left pointer is standing at the correct insert place
    return left
