"""
Given two lists that are sorted, return the median number between the two lists

[1, 2, 3] ~ len n
[2, 4, 5] ~ len m

[1, 2, 2, 3, 4, 5] => 2.5

We basically split the numbers into 2 equal groups such that all values in group A < values in group B
We start from the center of the list (smallest) and shift the slice points if not valid.
We take advantage of ordered nature of the lists.
"""


# TODO Untested
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        first_list = nums1
        second_list = nums2

        self.size_first = len(first_list)  # O(1) operation
        self.size_second = len(second_list)

        self.total_size = self.size_first + self.size_second
        is_even = (self.total_size % 2) == 0
        if not is_even:  # We want an extra element in the first half
            self.total_size += 1
        self.median_index = self.total_size / 2

        self.end_index = min(self.size_first, self.size_second)
        self.start_index = 0

        while True:
            self.update_indicies()
            median_found = self.median_found(first_list, second_list)
            if median_found:
                break
            self.start_index = self.intermediate_first_index + 1

        max_in_first_half = max(first_list[self.intermediate_first_index], second_list[self.intermediate_second_index])
        max_in_second_half = max(first_list[self.intermediate_first_index + 1], second_list[self.intermediate_second_index + 1])
        if not is_even:
            return max_in_first_half
        else:
            return (max_in_first_half + max_in_second_half) / 2

    def update_indicies(self):
        # All elements after nums1[intermediate_first_index] go into "group 2"
        self.intermediate_first_index = self.end_index + self.start_index / 2
        # All elements after nums2[intermediate_second_index] go into "group 2"
        self.intermediate_second_index = self.median_index - self.intermediate_first_index

    def median_found(self, first_list, second_list):
        """
        First half:
        A: [1, 2]
        B: [2, 4]
        Second Half:
        A: [3]
        B: [5]

        We want to ensure Last_A_First <= First_B_Second and Last_B_First <= First_A_Second
        """
        return \
            (first_list[self.intermediate_first_index] < second_list[self.intermediate_second_index + 1]) and \
            (second_list[self.intermediate_second_index] < first_list[self.intermediate_first_index + 1])

