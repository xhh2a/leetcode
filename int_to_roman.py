class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        symbol_map = {
            1000: 'M',
            500: 'D',
            100: 'C',
            50: 'L',
            10: 'X',
            5: 'V',
            1: 'I'
        }
        roman_string = ""
        base, _num = 1000, num
        while base:  # Works because of how division works in python 2 (integer division)
            digit, _num = divmod(_num, base)
            if digit == 9:
                roman_string += symbol_map[base] + symbol_map[base * 10]
            elif digit >= 5:
                roman_string += symbol_map[(base * 10) / 2] + symbol_map[base] * (digit - 5)
            elif digit == 4:
                roman_string += symbol_map[base] + symbol_map[(base * 10) / 2]
            elif digit >= 1:
                roman_string += symbol_map[base] * digit
            base /= 10
        return roman_string

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