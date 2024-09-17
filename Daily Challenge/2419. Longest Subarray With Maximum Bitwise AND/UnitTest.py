import unittest
from timeout_decorator import timeout
from Solution import Solution

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        self.testCases = {
            1: {'nums': [1,2,3,3,2,2], 'output': 2},
            2: {'nums': [1,2,3,4], 'output': 1}
        }
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        try:
            case = self.testCases[1]
            res = self.obj.longestSubarray(case['nums'])
            self.assertEqual(res, case['output'])
        except Exception as e:
            raise e
    
    @timeout(0.5)
    def test_Case2(self):
        try:
            case = self.testCases[2]
            res = self.obj.longestSubarray(case['nums'])
            self.assertEqual(res, case['output'])
        except Exception as e:
            raise e


if __name__ == '__main__':
    unittest.main()