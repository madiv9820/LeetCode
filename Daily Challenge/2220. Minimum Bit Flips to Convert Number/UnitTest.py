from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        self.testCases = {1: {'start': 10, 'goal': 7, 'output': 3},
                          2: {'start': 3, 'goal': 4, 'output': 3}}
        return super().setUp()
    
    def test_Case1(self):
        try:
            case = self.testCases[1]
            res = self.obj.minBitFlips(case['start'], case['goal'])
            self.assertEqual(res, case['output'])
        except Exception as e:
            raise e
        
    def test_Case2(self):
        try:
            case = self.testCases[2]
            res = self.obj.minBitFlips(case['start'], case['goal'])
            self.assertEqual(res, case['output'])
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    unittest.main()