from typing import Optional
import math

class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
           We can use pointers to insert the gcd of the
           two consecutive values of nodes between the
           nodes. We just need to keep track of the 
           current Node and next Node, so that we can find
           gcd to two nodes
        '''

        # Creating two pointers
        # current_Node is currently pointing
        # towards head/start of the linked list
        current_Node = head   

        # next_Node is pointing towards very next
        # node of the current node   
        next_Node = current_Node.next   

        # For inserting gcd between the node
        # we need the pair of the node, so we can
        # find the gcd, so running till we have a
        # consecutive pair
        while next_Node:
            # Finding gcd of the consecutive nodes
            gcd = math.gcd(current_Node.val, next_Node.val)
            
            # Since we have find gcd, we have to
            # insert between the pair nodes
            # First we have to disconnect both pair
            # and connect first node to newly created node

            # Creating a new node for gcd
            new_Node = ListNode(gcd)

            # Connecting first node to a newly
            # created node (ListNode(gcd))
            current_Node.next = new_Node

            # Once first node is connected to
            # newly created node, the newly created node
            # need to be connected with second node
            new_Node.next = next_Node
            
            # Now we have inserted gcd between the
            # consecutive pairs, we can move to next pair
            current_Node = next_Node
            next_Node = next_Node.next

        return head     # Returing head of modified linked list