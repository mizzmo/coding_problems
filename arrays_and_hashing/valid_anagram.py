# Valid Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.



# Attempt 1 - Sorting
# Time Complexity - O(n log n)
# Space Complexity - O(n)


class Solution0:
    def isAnagram(self, s: str, t: str) -> bool:
        # Contains the exact same characters in a different order.
        if len(s) != len(t):
            # If not same length, cant have same characters
            return False
        # Convert both the strings to arrays
        word_a = list(s)
        word_b = list(t)
        # Sort both arrays
        word_a.sort()
        word_b.sort()
        # Check if the arrays are the same
        if word_a != word_b:
            return False
        return True
    
    
    
# Attempt 2 - Hashmaps
# Time Complexity - O(n)
# Space Complexity - O(n)
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        # Quickly remove non-anagrams with differing lengths
        if len(s) != len(t):
            return False
        
        # Create two hashmaps to represent the number of each character
        a, b = {}, {}

        for i in range(0, len(s)):
            # For each character, check if it is in the hashmap and add +1 to total appearances.
            if s[i] in a:
                a[s[i]] = a[s[i]] + 1
            else:
                 a[s[i]] = 1
            # Same for other word.
            if t[i] in b:
                b[t[i]] = b[t[i]] + 1
            else:
                 b[t[i]] = 1

        # Check if equal
        if a != b:
            return False
        return True
        

# Model Answer
# Time Complexity - O(n+m)
# Space Complexity - O(1)
class SolutionM:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT