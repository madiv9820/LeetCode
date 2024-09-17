from Solution import Solution, ListNode
import unittest
from timeout_decorator import timeout
from typing import List, Optional

class UnitTest(unittest.TestCase):
    def __create_LL(self, ll_Values: List[int]) -> Optional[ListNode]:
        head = tail = None

        for value in ll_Values:
            if head: tail.next = ListNode(value); tail = tail.next
            else: head = tail = ListNode(value)

        return head
    
    def __create_Array(self, node: Optional[ListNode]) -> List[int]:
        array = []

        while node:
            array.append(node.val)
            node = node.next

        return array

    def setUp(self) -> None:
        self.obj = Solution()
        self.testCases = {
            1: {'head': [1,2,3], 'k': 5, 'output': [[1],[2],[3],[],[]]},
            2: {'head': [1,2,3,4,5,6,7,8,9,10], 'k': 3, 'output': [[1,2,3,4],[5,6,7],[8,9,10]]}
        }
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        test = self.testCases[1]
        k = test['k']
        output = test['output']
        try:
            head = self.__create_LL(test['head'])
            res = self.obj.splitListToParts(head, k)
            for i in range(len(res)):
                res[i] = self.__create_Array(res[i])
            self.assertEqual(res, output)
        except Exception as e:
            raise e

    @timeout(0.5)   
    def test_Case2(self):
        test = self.testCases[2]
        k = test['k']
        output = test['output']
        try:
            head = self.__create_LL(test['head'])
            res = self.obj.splitListToParts(head, k)
            for i in range(len(res)):
                res[i] = self.__create_Array(res[i])
            self.assertEqual(res, output)
        except Exception as e:
            raise e

if __name__ == '__main__':
    unittest.main()