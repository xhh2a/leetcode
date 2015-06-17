import collections


class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        order = [1, 5, 10, 50, 100, 500, 1000]
        symbol_map = {
            1000: 'M',
            500: 'D',
            100: 'C',
            50: 'L',
            10: 'X',
            5: 'V',
            1: 'I'
        }
        pre_numbers = [4, 9]

        def _get_base_index(_num):
            """
            Return the index of the symbol that is lower than NUM
            """
            _res = len(order) - 1
            for i in xrange(len(order)):
                if _num < order[i]:
                    _res = i - 1
                    break
            return _res

        def _get_symbol(_index):
            return symbol_map[order[_index]]

        def _next_symbol(_index):
            return symbol_map[order[_index + 1]]

        def _get_singular_symbol(_char, _index):
            """
            Returns the "1"'s equivalent symbol based on base _INDEX for a given _CHAR
            """
            index_offset = 1 if _char > 5 else 0
            return _get_symbol(_index - index_offset)

        def _get_roman_string(_char, _num):
            base_index = _get_base_index(_num)
            if _char in pre_numbers:
                return _get_singular_symbol(_char, base_index) + _next_symbol(base_index)
            elif _char >= 5:
                result = _get_symbol(base_index)
                for _ in xrange(_char - 5):
                    result += _get_singular_symbol(_char, base_index)
                return result
            else:
                result = ""
                for _ in xrange(_char):
                    result += _get_symbol(base_index)
                return result

        reverse_order = str(num)[::-1]
        results = collections.deque([])
        multiple = 1
        for index, char in enumerate(reverse_order):
            num = int(char) * multiple
            results.appendleft(_get_roman_string(int(char), num))
            multiple *= 10
        return ''.join(results)

if __name__ == '__main__':
    sol = Solution()
    res = sol.intToRoman(1999)
    assert res == 'MCMXCIX', 'Expected MCMXCIX got ' + res
    res = sol.intToRoman(1066)
    assert res == 'MLXVI', 'Expected MLXVI got ' + res
    res = sol.intToRoman(768)
    assert res == 'DCCLXVIII', 'Expected DCCLXVIII got ' + res
    res = sol.intToRoman(1444)
    assert res == 'MCDXLIV', 'Expected MCDXLIV got ' + res
    res = sol.intToRoman(3333)
    assert res == 'MMMCCCXXXIII', 'Expected MMMCCCXXXIII got ' + res
    res = sol.intToRoman(3888)
    assert res == 'MMMDCCCLXXXVIII', 'Expected MMMDCCCLXXXVIII got ' + res
    res = sol.intToRoman(5)
    assert res == 'V', 'Expected V got ' + res