import unittest
from Solution import Solution

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()
        self.test_cases = {
            1: {'n': 3, 
                'edges': [[0,1],[1,2],[0,2]], 
                'succProb': [0.5,0.5,0.2], 
                'start': 0, 
                'end': 2,
                'Output': 0.25000},
            2: {'n': 3, 
                'edges': [[0,1],[1,2],[0,2]], 
                'succProb': [0.5,0.5,0.3], 
                'start': 0, 
                'end': 2,
                'Output': 0.30000},
            3: {'n': 3, 
                'edges': [[0,1]], 
                'succProb': [0.5], 
                'start': 0, 
                'end': 2,
                'Output': 0.00000}
        }
    
    def test_case1(self):
        test = self.test_cases[1]
        res = self.obj.maxProbability(test['n'], test['edges'],
                                       test['succProb'], test['start'], test['end'])
        self.assertAlmostEqual(res, test['Output'])
    
    def test_case2(self):
        test = self.test_cases[2]
        res = self.obj.maxProbability(test['n'], test['edges'],
                                       test['succProb'], test['start'], test['end'])
        self.assertAlmostEqual(res, test['Output'])
    
    def test_case3(self):
        test = self.test_cases[3]
        res = self.obj.maxProbability(test['n'], test['edges'],
                                       test['succProb'], test['start'], test['end'])
        self.assertAlmostEqual(res, test['Output'])

if __name__ == '__main__':
    unittest.main()