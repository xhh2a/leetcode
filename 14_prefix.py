"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minimum_length = min([len(_word) for _word in strs]) if len(strs) else 0
        if minimum_length:
            max_index = 0
            for i in range(0, minimum_length):
                expected_char = strs[0][i]
                all_match = True
                for _word in strs[1:]:
                    if _word[i] != expected_char:
                        all_match = False
                        break
                if not all_match:
                    break
                else:
                    max_index += 1
            return strs[0][:max_index]
        return ""

Solution().longestCommonPrefix(["flap", "flower"])