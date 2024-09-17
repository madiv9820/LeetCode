from typing import Optional
import math

class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
            We can solve this problem, using arrays.
            We can store all the values in nodes in arrays,
            and find the greatest common divisor between
            the two nodes, and create a new linked list.
        '''
        # Adding values from linked list in the array
        node_Values = []; temp = head
        while temp:
            node_Values.append(temp.val)
            temp = temp.next

        # Create head and tail of new list
        # Assing first value of node to 
        # new_Head and new_Tail
        new_Head = new_Tail = ListNode(node_Values[0])
        
        # Since it is given than we have insert
        # a node with gcd between two consecutive
        # nodes, so first we are finding gcd of the
        # two consecutive no's and creating node with
        # that value, and adding the next value of node
        # after.
        for index in range(1, len(node_Values)):
            # Finding the gcd between two
            # consecutive values
            gcd = math.gcd(node_Values[index-1],
                           node_Values[index])
            
            # Creating and adding a new node with
            # the value of gcd to the new linked list
            new_Tail.next = ListNode(gcd)
            new_Tail = new_Tail.next

            # Adding the value of current node to the
            # new linked list
            new_Tail.next = ListNode(node_Values[index])
            new_Tail = new_Tail.next

        # Returning head of newly linked list
        return new_Head