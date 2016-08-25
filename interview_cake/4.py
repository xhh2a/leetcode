import math

def merge_two(first, second):
    f_start, f_end = first
    s_start, s_end = second
    if f_start == s_start:
        return (f_start, max(f_end, s_end))
    elif s_start <= f_end:
        return (f_start, max(f_end, s_end))
    else:
        return None


def my_function(arg):
    """
    We sort by starting time and then merge after in incrementing order
    sorting using mergesort or timsort has nlogn time.
    nlogn + n ~ nlogn.
    """
    if not arg:
        return []
    sorted_results = sorted(arg, key=lambda first: first[0])
    print 'running with %s' % sorted_results
    cur_index = 0
    next_index = 1
    results = []
    while next_index < len(sorted_results):  # TODO Something about the last index
        print 'current index: %s, next_index: %s' % (cur_index, next_index)
        current_timeframe = sorted_results[cur_index]
        next_timeframe = sorted_results[next_index]
        print 'checking %s %s' % (next_timeframe[0], next_timeframe[1])
        merged_results = merge_two(current_timeframe, next_timeframe)
        if merged_results is not None:
            sorted_results[cur_index] = merged_results
        else:
            results.append(sorted_results[cur_index])
            cur_index = next_index
        next_index += 1
        if next_index >= len(sorted_results):
            results.append(sorted_results[cur_index])
            break
    return results
            
        

# run your function through some test cases here
# remember: debugging is half the battle!
print my_function([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
print my_function([(1, 2), (2, 3)])
print my_function([(1, 10), (2, 3), (4, 5)])
