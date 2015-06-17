class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows <= 1:
            return s
        results = [[] for i in range(numRows)]
        modNum = numRows + (numRows - 2)
        for loc, char in enumerate(s):
            mod = loc % modNum
            row = mod if mod < numRows else modNum - mod
            results[row].append(char)
        return ''.join(''.join(row) for row in results)

if __name__ == '__main__':
    sol = Solution()
    print(sol.convert('PAYPALISHIRING', 3))  # PAHNAPLSIIGYIR
    print(sol.convert('ABC', 2))  # ACB
    print(sol.convert('ABCDEFG', 4))  # AGBFCED

