class Solution(object):
    
    def rob_sub(self, index, nums, cache):
        if index == 0:
            cache[index] = nums[0]
        elif index == 1:
            cache[index] = max(nums[index], nums[index - 1])
        else:
            cache[index] = max(nums[index] + cache[index - 2], cache[index - 1])
        return cache[index]
            
        
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            original_length = len(nums)
            doubled_list = nums + nums
            break_index =  original_length - 1
            end_index = len(doubled_list) - 1
            first_run_cache = {}
            second_run_cache = {}
            for i in xrange(0, break_index):
                self.rob_sub(i, doubled_list[0:break_index], first_run_cache)
            for i in xrange(0, break_index):
                self.rob_sub(i, doubled_list[break_index:end_index], second_run_cache)
            return max(first_run_cache[break_index - 1], second_run_cache[break_index - 1])
        