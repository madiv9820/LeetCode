import unittest
from Solution import Solution
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        self.testCases = {
            1: {'s': "zbax", 'k': 2, 'output': 8},
            2: {'s': "iiii", 'k': 1, 'output': 36},
            3: {'s': "leetcode", 'k': 2, 'output': 6},
            4: {'s': "skmgsaqwjkzrxufklvqarkejpshc", 'k': 10, 'output': 1}
        }
        return super().setUp()
    
    @timeout(0.5)
    def test_Case_1(self):
        test = self.testCases[1]
        res = self.obj.getLucky(test['s'], test['k'])
        
        self.assertIsInstance(res, int)
        self.assertEqual(res, test['output'])

    @timeout(0.5)
    def test_Case_2(self):
        test = self.testCases[2]
        res = self.obj.getLucky(test['s'], test['k'])
        
        self.assertIsInstance(res, int)
        self.assertEqual(res, test['output'])

    @timeout(0.5)
    def test_Case_3(self):
        test = self.testCases[3]
        res = self.obj.getLucky(test['s'], test['k'])
        
        self.assertIsInstance(res, int)
        self.assertEqual(res, test['output'])

    @timeout(0.5)
    def test_Case_4(self):
        test = self.testCases[4]
        res = self.obj.getLucky(test['s'], test['k'])
        
        self.assertIsInstance(res, int)
        self.assertEqual(res, test['output'])

if __name__ == '__main__':
    unittest.main()