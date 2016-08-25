import operator

OPERATORS_TO_SYMBOL = {
    '-',
    '+',
    '*',
    None
}


class Result(object):

    def __init__(self, starting_value):
        self.steps = starting_value

    def add(self, op, next_value):
        if op is not None:
            return Result(self.steps + [op, next_value])
        else:
            previous_values = self.steps[:-1]
            previous_values.append(int(unicode(self.steps[-1]) + unicode(next_value)))
            return Result(previous_values)

    def get_string(self):
        return ''.join([unicode(step) for step in self.steps])

    def is_valid(self, desired_length):
        return len(''.join([unicode(x) for x in self.steps if x not in OPERATORS_TO_SYMBOL])) == desired_length

    def __unicode__(self):
        return self.get_string()

    def __repr__(self):
        return self.get_string()


class Solution(object):

    @staticmethod
    def split_first_and_remaining(numbers):
        """
        Given a LIST of NUMBERS returns the first number and the remaining numbers
        """
        return numbers[0], numbers[1:]

    @staticmethod
    def _iter(fringe, all_permutations, numbers, end_index, target):
        """
        Takes a fringe of (PREVIOUS_VALUES, REMAINING_VALUES) where PREVIOUS_VALUES is a list of previously
        iterated permutations and REMAINING_VALUES are numbers that have not been iterated. Performs an iterative building
        of all permutations with OPERATORS inserted in between. If there are no REMAINING_VALUES,
        adds the built up permutations to ALL_PERMUTATIONS
        """
        previous_result, index = fringe.pop()
        if index == end_index:  # We are at the end of the list of numbers, add it to the results list
            result_string = unicode(previous_result)
            if eval(result_string) == target and previous_result.is_valid(end_index):
                all_permutations.add(result_string)
        else:
            next_number = numbers[index]
            for op in OPERATORS_TO_SYMBOL:
                new_result = previous_result.add(op, next_number)
                fringe.append((new_result, index + 1))

    def addOperators(self, num, target):
        """
        Given a string NUM of numbers, returns the permutations of +, -, * and no-op operations that add up to TARGET.
        """
        if not num or not isinstance(num, basestring):
            return []
        numbers = [int(number) for number in num]
        result_set = set()
        fringe = [(Result([numbers[0]]), 1)]  # Start number, remaining numbers
        desired_length = len(num)
        while len(fringe):
            self._iter(fringe, result_set, numbers, desired_length, target)
        return result_set

if __name__ == '__main__':
    solution = Solution()
    solution.addOperators("3456237490", 9191)
    # results = solution.addOperators("123", 6)
    # assert len(results) == 2
    # assert "1+2+3" in results
    # assert "1*2*3" in results
    # results = solution.addOperators("232", 8)
    # assert len(results) == 2
    # assert "2*3+2" in results
    # assert "2+3*2" in results
    # results = solution.addOperators("105", 5)
    # assert len(results) == 2
    # assert "1*0+5" in results
    # assert "10-5" in results
    # results = solution.addOperators("00", 0)
    # assert len(results) == 3
    # assert "0+0" in results
    # assert "0*0" in results
    # assert "0-0" in results
