from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        self.testCases = {
            1: {'arr': [1,3,4,8], 'queries': [[0,1],[1,2],[0,3],[3,3]], 'output': [2,7,14,8]},
            2: {'arr': [4,8,2,10], 'queries': [[2,3],[1,3],[0,0],[0,3]], 'output': [8,0,4,4]}
        }
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        try:
            case = self.testCases[1]
            res = self.obj.xorQueries(case['arr'], case['queries'])
            self.assertEqual(res, case['output'])
        except Exception as e:
            raise e
    
    @timeout(0.5)
    def test_Case2(self):
        try:
            case = self.testCases[2]
            res = self.obj.xorQueries(case['arr'], case['queries'])
            self.assertEqual(res, case['output'])
        except Exception as e:
            raise e
    

if __name__ == '__main__':
    unittest.main()