from typing import Optional, List
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
        We can solve this problem using binary tree traversal and
        depth first search (DFS) traversal. We can use DFS, to check
        the current downward path is the same as of linked list.
    '''
    def isSubPath(self, 
                    head: Optional[ListNode], 
                    root: Optional[TreeNode]) -> bool:
        # If root is null or None
        if not root: return False
        '''
            - Case 1: We will searching the whether the linked list is 
            starting from root.
            - Case 2: If we don't find the linked list starting from root,
            check for left subtree.
            - Case 3: If we don't find the linked list starting from root as
            well as left subtree, check from right subtree.
        '''
        return (self.depth_First_Search(head, root)
                    or self.isSubPath(head, root.left)
                    or self.isSubPath(head, root.right))
    
    # Depth First Search Algorithm
    def depth_First_Search(self, 
                node: Optional[ListNode], 
                root: Optional[TreeNode]) -> bool:
        # If node in the linked list 
        # is alreay completed or empty
        if not node: return True

        # If we have node in linked list but
        # node in tree is ended or values are not equal
        if not root or root.val != node.val: return False

        # Check for the next values in the node
        return (self.depth_First_Search(node.next, root.left) 
                    or self.depth_First_Search(node.next, root.right))