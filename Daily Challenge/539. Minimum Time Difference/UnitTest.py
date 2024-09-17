import unittest
from Solution2 import Solution
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        self.testCases = {1: {'timePoints': ["23:59","00:00"], 'output': 1},
                          2: {'timePoints': ["00:00","23:59","00:00"], 'output': 0}}
        return super().setUp()
    
    def test_Case1(self):
        try:
            case = self.testCases[1]
            res = self.obj.findMinDifference(case['timePoints'])
            self.assertEqual(res, case['output'])
        except Exception as e:
            raise e
        
    def test_Case2(self):
        try:
            case = self.testCases[2]
            res = self.obj.findMinDifference(case['timePoints'])
            self.assertEqual(res, case['output'])
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    unittest.main()