"""
Check if an integer is a palindrome or not without converting to string
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        else:
            intermediate = x
            digits = []
            while intermediate > 0:
                mul, rem = divmod(intermediate, 10)
                digits.append(rem)
                intermediate = mul
            return digits[::-1] == digits

Solution().isPalindrome(121)