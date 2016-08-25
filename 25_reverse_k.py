# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def is_group_valid(node, k):
    """
    Returns if the next K elements exists in a list given a NODE
    """
    counter = 0
    while node.next is not None and counter < k:
        node = node.next
        counter += 1
    return counter == k
    
def reverse_group(group_head, k):
    """
    Reverses a group of length K given a GROUP_HEAD, returning the new HEAD, new TAIL, and the next element that was detached.
    """
    counter = 0
    group_head.next = None
    previous_node = group_head
    next_node = previous_node.next_node
    while counter < k:
        new_next_node = new_node.next
        next_node.next = previous_node
        previous_node = next_node
        next_node = new_next_node
    return previous_node, group_head, next_node

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or head is None or head.next is None:
            return head
        group_head = head
        while is_group_valid(group_head, k):
            new_head, new_tail, next_element = reverse_group(group_head, k)
            # Fix group pointers