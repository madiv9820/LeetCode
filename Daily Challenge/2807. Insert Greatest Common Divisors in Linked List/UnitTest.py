from Solution1 import Solution, ListNode
import unittest
from timeout_decorator import timeout
from typing import Optional, List

class UnitTest(unittest.TestCase):
    def __create_LL(self, ll_Nodes: Optional[ListNode]) -> Optional[ListNode]:
        head = tail = None

        for val in ll_Nodes:
            if head: tail.next = ListNode(val); tail = tail.next
            else: head = tail = ListNode(val)

        return head

    def ___create_Array(self, node: Optional[ListNode]) -> List[int]:
        array = []

        while node:
            array.append(node.val)
            node = node.next

        return array

    def setUp(self):
        self.obj = Solution()
        self.testCase = {1: {'head': [18,6,10,3], 'output': [18,6,6,2,10,1,3]},
                         2: {'head': [7], 'output': [7]}}

    @timeout(0.5)
    def test_Case1(self):
        try:
            test = self.testCase[1]
            head = self.__create_LL(test['head'])
            res = self.obj.insertGreatestCommonDivisors(head)
            output = self.___create_Array(res)
            self.assertEqual(output, test['output'])
        except Exception as e:
            raise e
        
    @timeout(0.5)
    def test_Case2(self):
        try:
            test = self.testCase[2]
            head = self.__create_LL(test['head'])
            res = self.obj.insertGreatestCommonDivisors(head)
            output = self.___create_Array(res)
            self.assertEqual(output, test['output'])
        except Exception as e:
            raise e

    
if __name__ == '__main__':
    unittest.main()