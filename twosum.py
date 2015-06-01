class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        def _update_cache(_cache, _remainder, _index):
            if _remainder not in _cache:
                _cache[_remainder] = []
            _cache[_remainder].append(_index)
        cache = dict()
        for index, value in enumerate(nums):
            remainder = target - value
            if value in cache:
                return sorted([index + 1, cache[value].pop() + 1])
            else:
                _update_cache(cache, remainder, index)

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([0, 1, 2], 3))
    print(sol.twoSum([0, 2, 1, 0], 0))
    print(sol.twoSum([-3, 1, 4, 3], 0))
