class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        maximum = 0
        first_line = 0
        last_line = len(height) - 1

        def area(indexa, indexb):
            return min(height[indexa], height[indexb]) * abs(indexa - indexb)

        while first_line != last_line:
            maximum = max(maximum, area(first_line, last_line))
            start_shorter = height[first_line] < height[last_line]
            first_line = first_line + 1 if start_shorter else first_line
            last_line = last_line if start_shorter else last_line - 1
        return maximum

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxArea([1, 2, 1]))  # 2
    print(sol.maxArea([1, 2, 4, 3]))  # 4

