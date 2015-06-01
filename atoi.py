import re


class Solution:
    _filter = re.compile('\s*(\+?)(\-?)(\d+).*')

    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        filtered = Solution._filter.match(str)
        if filtered is not None:
            (positive, negative, val) = filtered.groups()
            if positive and negative:
                return 0
            if val:
                ret = int(val)
                ret = ret if ret < pow(2, 31) else ret if ret <= pow(2, 31) and negative else pow(2, 31) if negative else pow(2, 31) - 1
                return -ret if negative else ret
        return 0

if __name__ == '__main__':
    sol = Solution()
    print(sol.myAtoi("12345"))
    print(sol.myAtoi("  1234"))
    print(sol.myAtoi("  12345ead"))
    print(sol.myAtoi("  +12345"))
    print(sol.myAtoi("-12345"))
    print(sol.myAtoi("+-12346"))
    print(sol.myAtoi("2147483648"))
    print(sol.myAtoi("-2147483648"))