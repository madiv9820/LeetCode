from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        '''
            Since it is given that, length of words <= 10^4, we can use nested
            loop, to search for each character of word in words in present in
            allowed or not, if all the character of word, then it is consistent
            string else not.

            Time Complexity: O(X * Y * Z), where X is the length of words,
            average Y is the length of each word in words, Z is the length of
            allowed
            
            Space Complexity: O(1), we are not using any array/list/set/dictionary
        '''
        # Intialising value as 0
        consistent_Strings = 0

        # Iterating through each word in words
        for word in words:
            # Assuming all characters in word 
            # are already present in allowed
            all_Characters_Present = True

            # Now, checking each character in word
            for character in word:
                # If character is not present, then
                # the word is not consistent string
                if character not in allowed: 
                    all_Characters_Present = False 
                    break   # We don't need to check further, hence break
            
            # If all characters present in allowed,
            # then incrementing consistent_Strings
            if all_Characters_Present: consistent_Strings += 1

        # Returning total no of consistent strings
        return consistent_Strings