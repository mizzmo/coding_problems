# Encode and Decode Strings
#Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
#Please implement encode and decode


# Attempt 1 - Using # and letter count as a separator
# Time Complexity - O(n+m)
# Space Complexity - O(n+m)
class Solution0:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        long_string = "#"
        for string in strs:
            # Encode using # followed by the number of letters in that word.
            word_len = len(string)
            long_string += (str(word_len) + "#" + string + '#')
        return long_string

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        output_array = []
        i = 0
        word, word_length = "", 0
        while i < len(s):
            # Find each #
            length_string = ""
            if s[i] == '#' and (i + 1) < len(s):
                # Next word, read word length
                while s[i + 1].isdigit(): 
                    # Move to the next digit
                    i = i + 1
                    # Format as string and convert to int when complete number is there
                    length_string = length_string + s[i]
                    # Track the current index.
                    
            # Move on to the first letter, skipping the separating
            i = i + 2       
            # Move onto next letter
            if len(length_string) > 0:
                word_length = int(length_string)
            else:
                break
            
            # Loop through that many letters to get the next word
            for j in range(0, word_length):
                word = word + s[i+j]
            
            # Add the completed word to the array
            output_array.append(word)
            # Clear the word
            word = ""
            # Update I to the next letter after the word.
            i = i + word_length

        return output_array
    
# Attempt 2 - 
# Time Complexity - O(n+m)
# Space Complexity - O(n+m)
class Solution1:

    def encode(self, strs: List[str]) -> str:
        # Join the strings together into a single string
        # Use a non letter character to separate the strings.
        # Include the length of each string
        output_string = "#"
        for string in strs:
            length = len(string)
            output_string = output_string + str(length) + "#" + string + "#"
        return output_string

    def decode(self, s: str) -> List[str]:
        # Look for each instance of the non-letter character.
        output = []
        word = ""
        i = 0
        print(s)
        while i < len(s)-1:
            # Hits the first hash, start of the next word.
            if s[i] == "#" and s[i+1].isdigit():
                # Account for strings longer than 9 characters
                length_string = ""
                while s[i+1].isdigit():
                    length_string = length_string + s[i+1]
                    i += 1

                length = int(length_string)
                # Skip the next two letters
                i = i + 2
                # Use the length to get the entire word
                for j in range(length):
                    word = word + s[i]
                    i = i + 1
                # Add the complete word to the output and reset the word.
                output.append(word)
                word = ""
            else:
                break

        return output


# Model Answer - 
# Time Complexity - O(m)
# Space Complexity - O(m+n)
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res