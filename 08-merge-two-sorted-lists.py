class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        # Step 1: Create a dummy head (fake node)
        dummy = ListNode(-1)
        
        # Step 2: A pointer to build the new list
        current = dummy
        
        # Step 3: Compare until one list is empty
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next  # move forward
        
        # Step 4: Attach the rest of whichever list is left
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        # Step 5: Return the merged list (skip the dummy node)
        return dummy.next
