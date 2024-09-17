from typing import List, Optional
import unittest
from timeout_decorator import timeout
from Solution import Solution, TreeNode, ListNode
from collections import deque

class UnitTest(unittest.TestCase):
    def create_LL(self, 
                    list_Nodes: List[int]) -> Optional[ListNode]:
        head = tail = None

        for node in list_Nodes:
            if head is None: head = tail = ListNode(node)
            else: tail.next = ListNode(node); tail = tail.next

        return head
    
    def create_Tree(self, tree_Nodes: List[int]) -> Optional[TreeNode]:
            root = TreeNode(tree_Nodes[0])
            queue = deque([root]); index = 1

            while queue and index < len(tree_Nodes):
                node = queue.popleft()
                if index < len(tree_Nodes):
                    if tree_Nodes[index] is not None:
                        node.left = TreeNode(tree_Nodes[index])
                        queue.append(node.left)
                    index += 1
                if index < len(tree_Nodes):
                    if tree_Nodes[index] is not None:
                        node.right = TreeNode(tree_Nodes[index])
                        queue.append(node.right)
                    index += 1

            return root

    def setUp(self) -> None:
        self.obj = Solution()
        self.testCases = {
            1: {
                'head': [4,2,8],
                'root': [1,4,4,None,2,2,None,1,
                         None,6,8,None,None,None,
                         None,1,3],
                'output': True
            },
            2: {
                'head': [1,4,2,6],
                'root': [1,4,4,None,2,2,None,1,
                         None,6,8,None,None,None,
                         None,1,3],
                'output': True
            },
            3: {
                'head': [1,4,2,6,8],
                'root': [1,4,4,None,2,2,None,
                         1,None,6,8,None,None,None,
                         None,1,3],
                'output': False
            }
        }
        return super().setUp()
    
    @timeout(0.5)
    def test_Case_1(self):
        test = self.testCases[1]
        ll_Nodes = test['head']
        tree_Nodes = test['root']
        output = test['output']
        try:
            head = self.create_LL(ll_Nodes)
            root = self.create_Tree(tree_Nodes)
            res = self.obj.isSubPath(head, root)
            self.assertEqual(res, output)
        except Exception as e:
            raise e

    @timeout(0.5)
    def test_Case_2(self):
        test = self.testCases[2]
        ll_Nodes = test['head']
        tree_Nodes = test['root']
        output = test['output']
        try:
            head = self.create_LL(ll_Nodes)
            root = self.create_Tree(tree_Nodes)
            res = self.obj.isSubPath(head, root)
            self.assertEqual(res, output)
        except Exception as e:
            raise e
    
    @timeout(0.5)
    def test_Case_3(self):
        test = self.testCases[3]
        ll_Nodes = test['head']
        tree_Nodes = test['root']
        output = test['output']
        try:
            head = self.create_LL(ll_Nodes)
            root = self.create_Tree(tree_Nodes)
            res = self.obj.isSubPath(head, root)
            self.assertEqual(res, output)
        except Exception as e:
            raise e


if __name__ == '__main__':
    unittest.main()