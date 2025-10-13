class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
       # j will keep track of the position to place valid elements
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:  # place the element at position j
                nums[j] = nums[i]
                j += 1  # move j forward
        return j
