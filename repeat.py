class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        maximumLength = startIndex = 0
        cache = dict()
        for i in range(len(s)):
            char = s[i]
            if char in cache and startIndex <= cache[char]:
                startIndex = cache[char] + 1  # The next possible longest value is after the last seen location of this character
            cache[char] = i  # Update the last seen location of this character
            maximumLength = max(maximumLength, i - startIndex + 1)  # Cannot put this in return statement for empty inputs.

        return maximumLength