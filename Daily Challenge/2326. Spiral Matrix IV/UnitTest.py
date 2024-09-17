from Solution import Solution, ListNode
import unittest
from timeout_decorator import timeout
from typing import List, Optional

class UnitTest(unittest.TestCase):
    def __create_LL(self, values: List[int]) -> Optional[ListNode]:
        head = tail = None

        for val in values:
            if head: tail.next = ListNode(val); tail = tail.next
            else: head = tail = ListNode(val)

        return head

    def setUp(self) -> None:
        self.obj = Solution()
        self.testCases = {
            1: {'m': 3, 'n': 5, 'head': [3,0,2,6,8,1,7,9,4,2,5,5,0],
                'output': [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]},
            2: {'m': 1, 'n': 4, 'head': [0,1,2], 'output': [[0,1,2,-1]]}
        }
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        try:
            test = self.testCases[1]
            head = self.__create_LL(test['head'])
            res = self.obj.spiralMatrix(test['m'], test['n'], head)
            self.assertTrue(len(res) == len(test['output']))
            self.assertTrue(len(res[0]) == len(test['output'][0]))
            self.assertEqual(res, test['output'])
        except Exception as e:
            raise e
    
    @timeout(0.5)
    def test_Case2(self):
        try:
            test = self.testCases[2]
            head = self.__create_LL(test['head'])
            res = self.obj.spiralMatrix(test['m'], test['n'], head)
            self.assertTrue(len(res) == len(test['output']))
            self.assertTrue(len(res[0]) == len(test['output'][0]))
            self.assertEqual(res, test['output'])
        except Exception as e:
            raise e

    
if __name__ == '__main__':
    unittest.main()