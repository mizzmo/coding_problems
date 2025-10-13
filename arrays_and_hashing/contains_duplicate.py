# My Solution ################################
# Uses a Hashmap to track the appearances of numbers
# by using the number as a key with the counter as a value.

# Time Complexity: O(n)
# Space Complexity: O(n)
# (Optimal)

class Solution:
    def hasDuplicate(self, nums) -> bool:
        # Declare a dictionary of equal length to the input array and populate with 0.
        tracker = {}
        
        for i in range(0,len(nums)):
            if nums[i] in tracker:
                # Check if the key is already in the dictionary and add to the counter
                tracker[nums[i]] = tracker[nums[i]] + 1
            else:
                # Add a new key
                tracker[nums[i]] = 1

        # Look for counters greater than 1 in the dictionary
        for value in tracker.values():
            if value > 1:
                return True
            
        return False


# Optimal Solution ################################

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def hasDuplicate(self, nums) -> bool:
        # Convert the array to a set, this removes duplicate items.
        # Compare the lengths of the two data structures.
        # If they are different then an item has been removed meaning there was a duplicate present
        return len(set(nums)) < len(nums)