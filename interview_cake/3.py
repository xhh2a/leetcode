from collections import deque

def my_function(arg):
    """
    Keep track of: Lowest 2 negative numbers, Lowest 2 positive numbers, Largest 3 positive numbers
    "Highest" product is max between:
      - Lowest 2 negative numbers * largest positive number
      - Largest 3 positive numbers
      - Highest negative number * lowest 2 positive numbers
    """
    # write the body of your function here
    print 'running with %s' % arg
    if len(arg) == 3:
        result = 1
        for i in arg:
            result *= i
        return result
    highest_values = []
    highest_negative_values = []
    lowest_high_value = None
    lowest_negative_value = None
    for number in arg:
        if number >= 0:
            print 'lowest_high_value is %s' % lowest_high_value
            if len(highest_values) < 3 or or lowest_high_value < number:
                print 'adding to stack %s' % number
                highest_values.append(number)
                if lowest_high_value is None:
                    lowest_high_value = number
                else:
                    lowest_high_value = min(highest_values)
                if len(highest_values) > 3:
                    removed = highest_values.remove(lowest_value)
                    print 'removed %s' % lowest_value
         else:
            print 'checking negative_numbers'
            if len(highest_negative_values) < 2 or lowest_negative_value > number:
                print 'adding to negative stack %s' % number
                highest_negative_values.append(number)
                # TODO
    result = 1
    for i in arg:
        result *= i
    return result

print my_function([1, 2, 3])
print my_function([2, 2, 2])
print my_function([3, 1, 2, 2])
print my_function([4, 5, 2, 9, 10])