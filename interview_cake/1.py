def my_function(arg):
    # write the body of your function here
    print 'running with %s' % arg
    if len(arg) < 2:
        raise Exception("Invalid amount of inputs")
    elif len(arg) == 2:
        return arg[1] - arg[0] 
    maximum_value = None
    minimum_value = arg[0]
    for value in arg[1:]:
        if value < minimum_value:
            minimum_value = value
        elif maximum_value is None and value > minimum_value:
            maximum_value = value
        elif maximum_value is not None and value > maximum_value:
            maximum_value = value
    if not maximum_value:
        return minimum_value - arg[0]
    else:
        return maximum_value - minimum_value

# run your function through some test cases here
# remember: debugging is half the battle!
print my_function([1, 2, 3])
print my_function([1, 2, 3, 1, 5])
print my_function([2, 3])
print my_function([5, 4, 3, 2, 1])
