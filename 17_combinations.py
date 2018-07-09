"""
Given a telephone list of possible digits, return possible word combinations
"""
#from itertools import product


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        number_to_letter = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        possible_letters = [number_to_letter.get(number, None) for number in digits]
        return [''.join(x) for x in self.product(*possible_letters)]

    def product(self, *combinations):
        # Leetcode doesn't allow using product
        res = [[]]
        for combination in combinations:
            res = [cur + [_next] for cur in res for _next in combination]
        return res

Solution().letterCombinations("23")