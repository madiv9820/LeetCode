from typing import List, Optional

class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, 
                            head: Optional[ListNode], 
                            k: int) -> List[Optional[ListNode]]:
        '''
            To split the linked list into k parts, we need to
            calculate no of nodes for each part, plus we need
            to extra node at each part if k is not completely
            divisible with N.

            We can use pointers, to solve this problem and add
            the node to the list and array.

            Time Complexity: O(N), where N is the no of nodes 
            in the linked list
            
            Space Complexity: O(1)
        '''

        # Calculating the length of the linked list
        N = 0 
        temp = head
        while temp: 
            N += 1 
            temp = temp.next

        # Calculating the required variables
        no_of_Nodes_In_Each_Part = N // k
        # If k < N, we do not have any extra node to add
        no_of_Parts_With_Extra_Node = (N % k) if N > k else 0
        
        parts = []  # List of nodes after splitting

        # Dividing the list in k parts
        for _ in range(k):
            # Adding Node to the array
            parts.append(head)
            # Splitting the linked list
            if head:
                # Moving node  
                for _ in range(no_of_Nodes_In_Each_Part-1): 
                    head = head.next
                    if not head: 
                        break
                
                # Adding extra node to the part
                if no_of_Parts_With_Extra_Node: 
                    head = head.next
                    no_of_Parts_With_Extra_Node -= 1
                
                if not head: 
                    break
                
                # Now we have n nodes in the part
                # We can cut the linked list
                next_Node = head.next
                head.next = None
                head = next_Node

        return parts    # Returning the splitted Linked List

def __create_LL(ll_Values: List[int]) -> Optional[ListNode]:
        head = tail = None

        for value in ll_Values:
            if head: tail.next = ListNode(value); tail = tail.next
            else: head = tail = ListNode(value)

        return head
    
def __create_Array(node: Optional[ListNode]) -> List[int]:
    array = []

    while node:
        array.append(node.val)
        node = node.next

    return array

if __name__ == '__main__':
    head = [1,2,3,4,5,6,7,8,9,10]; k = 6
    head = __create_LL(head)
    sol = Solution()

    res = sol.splitListToParts(head, k)
    for i in range(len(res)):
        res[i] = __create_Array(res[i])

    print(res)