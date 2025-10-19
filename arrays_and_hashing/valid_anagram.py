# My Solution

class Solution:
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
        for i in range(0, len(word_a)):
            if word_a[i] == word_b[i]:
                continue
            else:
                return False

        return True