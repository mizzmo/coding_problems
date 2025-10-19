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
        
        