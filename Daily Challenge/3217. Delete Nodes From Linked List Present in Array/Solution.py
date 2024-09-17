from typing import List, Optional

class ListNode:
    def __init__(self, val = None, next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, 
                        nums: List[int], 
                        head: Optional[ListNode]) -> Optional[ListNode]:
        '''
            Approach:- We will be using pointers to set the connection
            between the nodes. Rather than creating a seperate new LL,
            we will be deleting nodes in the given list, which will reduce
            space complexity.

            Time Complexity: O(N + M)
            where:
                1. N is the no of nodes in the linked  list.
                2. M is the size of the nums, since nums is list
                or array, we will be converting nums to a hashset,
                so that search operations become faster.
            Space Complexity: O(1), since we are not using any space
            other than creating variables
        '''
        # Using pointer for the node
        # We are taking two pointers:- current and previous
        # which currently points to head and None respectively
        current_Node = head; previous_Node = None

        # Converting nums to a hashset
        nums = set(nums)

        # Traversing through each node
        while current_Node:
            '''
                If value is present in nums, which means
                we need to delete this node, or remove this
                node from the linked list, else we can ignore it
            '''
            if current_Node.val in nums:
                if current_Node == head: 
                    '''
                        If node to be removed is head, 
                        so need to update the head
                    '''
                    head = current_Node.next
                else:
                    '''
                        Since previous node is just previous to the
                        current node, and we need to remove the
                        current node, we first to need to connect
                        previous node to next node of current  
                    '''
                    previous_Node.next = current_Node.next                   
            else: 
                '''
                    If value is not present in nums, we need to check for
                    next node, but moving to next node, we need to update
                    previous node.
                '''
                previous_Node = current_Node

            # Moving to next node    
            current_Node = current_Node.next

        # Returning the head of modified list
        return head     