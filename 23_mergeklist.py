from queue import PriorityQueue

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 1:
            return lists[0]
        else:
            queue = PriorityQueue()
            result = None
            tail = None
            for index, list in enumerate(lists):  # Initialize queue
                if list is not None:
                    queue.put((list.val, list, index))
                    lists[index] = list.next
            while not queue.empty():
                _, element, list_index = queue.get()
                if tail is None:  # Update next elements
                    result = tail = element
                else:
                    tail.next = element
                    tail = element
                tail.next = None  # Clear tail's next to empty
                # Add the next element from the lists to the queue
                next_element = lists[list_index]
                if next_element is not None:
                    queue.put((next_element.val, next_element, list_index)) 
                    lists[list_index] = next_element.next  # Update list index to next
            