# Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.

# Attempt 1 - Hashmap / Heap
class Solution0:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a hashmap to store a counter for each number in the list.
        counts = {}
        for i in range(len(nums)):
            # Add the number of occurances to the hashmap
            if nums[i] in counts:
                counts[nums[i]] += 1
            else:
                counts[nums[i]] = 1

        # Use the hashmap to find the numbers with the highest count.
        # Array to store the output, of length k
        output_arr = [0] * k
        
        # Repeat for K
        for j in range(k):
            # Track the higest occurances and which key that corresponds to
            highest_occurences = 0
            highest_key = 0
            for key in counts.keys():
                if counts[key] > highest_occurences:
                    highest_occurences = counts[key]
                    highest_key = key
            # Remove the key from the hashmap
            counts.pop(highest_key)
            # Add the highest key to the output array
            output_arr[j] = highest_key
        return output_arr
    
    
# Model Solution - Bucket Sort

class SolutionM:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res