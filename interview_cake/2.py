def my_function(arg):
    # write the body of your function here
    print 'running with %s' % arg
    multiplier = 1
    results = [1] * len(arg)
    for i in xrange(0, len(arg)):
        results[i] *= multiplier
        multiplier *= arg[i]
    print 'intermediate results %s' % results
    multiplier = 1
    for i in xrange(len(arg) - 1, -1, -1):
        results[i] *= multiplier
        multiplier *= arg[i]
    return results

# run your function through some test cases here
# remember: debugging is half the battle!
print my_function([1, 7, 3, 4])
print my_function([0, 1, 3, 4])
