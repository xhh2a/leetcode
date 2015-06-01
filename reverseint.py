class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        negative = x < 0
        x = -x if negative else x
        res = int(str(x)[::-1])
        return 0 if res >= pow(2, 31) else -res if negative else res

if __name__ == '__main__':
    sol = Solution()
    print(sol.reverse(12345))
    print(sol.reverse(1234678901234567890))