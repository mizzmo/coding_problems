# Group Anagrams
# Given an array of strings strs, group all anagrams together into sub-lists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Attempt 1 - Hashmap and Array word Count
# Time Complexity - O(m * n)
# Space Complexity - O(m)
class Solution0:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Handle the case that there is only one word.
        if(len(strs) == 1):
            print(list([strs[0]]))
            return list([strs])

        # Create a hashmap for each possible anagram
        anagrams = {}
        # For every word in the list
        for i in range(len(strs)):
            characters = [0] * 26
            for character in strs[i]:
                # Count each value in an array, indexed by the character number in alphabet
                characters[ord(character) - ord('a')] += 1

            # If the array is in the hashmap, add a new word to the list
            if tuple(characters) in anagrams:
                anagrams[tuple(characters)].append(strs[i])
            # Otherwise make a new list
            else:
                anagrams[tuple(characters)] = list([strs[i]])
        # Return the list of values in the hashmap
        return list(anagrams.values())
    
    
    
# Model Answer - Hashmap and Array word Count
# Time Complexity - O(m * n)
# Space Complexity - O(m)

class SolutionM:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
