import unittest
from timeout_decorator import timeout
from Solution import Solution

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        self.testCases = {
            1: {'commands': [4,-1,4,-2,4], 'obstacles': [[2,4]], 'output': 65},
            2: {'commands': [6,-1,-1,6], 'obstacles': [], 'output': 36},
            3: {'commands': [4,-1,3], 'obstacles': [], 'output': 25}
        }
        return super().setUp()
    
    @timeout(0.5)
    def testCase1(self):
        try:
            test = self.testCases[1]
            res = self.obj.robotSim(test['commands'], test['obstacles'])
            self.assertIsInstance(res, int)
            self.assertEqual(res, test['output'])
        except Exception as e:
            raise e
    
    @timeout(0.5)
    def testCase2(self):
        try:
            test = self.testCases[2]
            res = self.obj.robotSim(test['commands'], test['obstacles'])
            self.assertIsInstance(res, int)
            self.assertEqual(res, test['output'])
        except Exception as e:
            raise e
    
    @timeout(0.5)
    def testCase3(self):
        try:
            test = self.testCases[3]
            res = self.obj.robotSim(test['commands'], test['obstacles'])
            self.assertIsInstance(res, int)
            self.assertEqual(res, test['output'])
        except Exception as e:
            raise e

if __name__ == '__main__':
    unittest.main()
