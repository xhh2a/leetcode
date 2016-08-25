class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        found_vowels = []
        VOWELS = {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u"}
        intermediate = []
        for letter in s:
            if letter in VOWELS:
                found_vowels.append(letter)
                intermediate.append(None)
            else:
                intermediate.append(letter)
        result = []
        for letter in intermediate:
            if letter:
                result.append(letter)
            else:
                result.append(found_vowels.pop())
        return ''.join(result)