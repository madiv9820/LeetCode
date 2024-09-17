from typing import List, Optional

class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, 
                        m: int, 
                        n: int, 
                        head: Optional[ListNode]) -> List[List[int]]:
        # Creating a (m X n) matrix, 
        # with initial values as -1
        matrix = [[-1] * n for _ in range(m)]

        # Creating pointers to check, for the
        # range of what is top row, last row
        # left column and right columns.
        start_Row = 0; end_Row = m-1
        start_Col = 0; end_Col = n-1

        # Traversing through each node
        while head:
            '''
                Since the direction of the spiral, as
                left -> right, up -> down, right -> left,
                down -> up, we will be filling our matrix as
                in the same direction starting from top row and
                left column.
            '''
            # Traversing from left to right
            for index in range(start_Col, end_Col+1):
                # Assigning the value 
                matrix[start_Row][index] = head.val
                
                # Moving to next node
                head = head.next

                # An edge case if linked list ends
                if not head: break

            # Since we have to filled our top
            # row, we need to change the top row
            # Hence, moving to next row
            start_Row += 1

            # If list is empty, we can end the iteration
            if not head: break

            # Traversing from up to down, current pointer
            # would be at end_Col, hence filling last column
            for index in range(start_Row, end_Row+1):
                matrix[index][end_Col] = head.val
                head = head.next
                if not head: break

            # Last Column has been filled, 
            # hence updating last column
            end_Col -= 1
            if not head: break
            
            # Now pointer is at end_Row, filling end_Row but 
            # from right to left.
            for index in range(end_Col, start_Col-1, -1):
                matrix[end_Row][index] = head.val
                head = head.next
                if not head: break
            
            # Last Row has been filled,
            # hence updating the last row
            end_Row -= 1
            if not head: break

            # Now pointer is at start_Col, filling start_Col but
            # from down to up
            for index in range(end_Row, start_Row-1, -1):
                matrix[index][start_Col] = head.val
                head = head.next
                if not head: break

            # Updating starting column
            start_Col += 1
            if not head: break

        return matrix   # Returning the matrix