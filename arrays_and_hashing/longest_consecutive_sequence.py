
# Attempt 1: Sets and Sorting
# Time Complexity - O(n log n)
# Space Complexity - O(n)
class Solution0:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        # Store the highest value of consecutive numbers
        highest_consec = 0
        # Convert the input to a set to remove duplicates
        nums = set(nums)
        # Convert the set back to a list and sort it.
        nums = list(nums)
        nums.sort()
        # Iterate through the list once, recording each set of consecutive numbers
        prev_number = nums[0]
        current_consec = 0
        for number in nums:
            if number == prev_number + 1:
                current_consec += 1
                # Update the previous number for the next iteration
                prev_number = number
            else:
                current_consec = 1
                prev_number = number

            # Check if the current consecutive sequence is greater than the current highest.
            if current_consec > highest_consec:
                highest_consec = current_consec 

        return highest_consec           
    
    
# Attempt 2: Sets
# Time Complexity - O(n)
# Space Complexity - O(n)
class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Store longest consecutive length
        longest_consec = 0
        # Convert the input to a set.
        number_set = set(nums)

        current_consec = 0
        # Iterate through the set.
        for number in number_set:
            # Check if the number before is in the set.
            if number - 1 in number_set:
                current_consec = 2
                current_num = number -1
                # If so, add one to consec, look for the number before that number.
                while current_num - 1 in number_set:
                    # Decrement current number, increment current consec.
                    current_num -= 1
                    current_consec += 1
            else:
                current_consec = 1
            if current_consec > longest_consec:
                longest_consec = current_consec

        return longest_consec
    
    
# Model Solution: Hash Map
# Time Complexity - O(n)
# Space Complexity - O(n)

class SolutionM:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res
  