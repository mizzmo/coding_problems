# Two Sum
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# First Attempt - Loop through every value.
# Time Complexity - O(n^2)
# Space Complexity - O(1)

class Solution0:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Two pointers, check every possible combination of sums, stop when found.
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                # Skip equal numbers
                if i == j:
                    continue
                elif (nums[i] + nums[j]) == target:
                    return [i,j]
                
                
# Second Attempt - Using Target Difference to find a result.
# Time Complexity - O(n^2)
# Space Complexity - O(1)
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Starting with the target, subtract every value for i, and look for a value of j that matches the result
        for i in range(0, len(nums)):
            search_term = target - nums[i]
            # Find a matching j in the list
            for j in range(1, len(nums)):
                if i != j and nums[j] == search_term:
                    return [i,j]
                

# Third Attempt - Using a Hashmap combined with Difference
# Time Complexity - O(n)
# Space Complexity - O(n)
# (Optimal)

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Declare a hashmap to store our progress
        progress = {}
        # Starting with the target, subtract every value for i, and look for a value of j that matches the result
        for i in range(0, len(nums)):
            search_term = target - nums[i]
            # Check if the search term is in the hash map already.
            if search_term in progress:
                return [progress[search_term], i]
            else:
                # Otherwise add nums[i] to the hashmap and store its index.
                progress[nums[i]] = i
                
                
# Model Answer - Hash Map (One Pass)
# Time Complexity - O(n)
# Space Complexity - O(n)
class SolutionM:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i