import unittest
from Solution import Solution

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()
        self.testCases = {
            '1': {'original': [1,2,3,4],
                    'm': 2, 'n': 2,
                    'output': [[1,2],[3,4]]},
            '2': {'original': [1,2,3],
                    'm': 1, 'n': 3,
                    'output': [[1,2,3]]},
            '3': {'original': [1,2],
                    'm': 1, 'n': 1,
                    'output': []}
        }

    def test_Case1(self):
        testCase = self.testCases['1']
        res = self.obj.construct2DArray(testCase['original'],
                            testCase['m'], testCase['n'])
        
        self.assertIs(type(res), list)
        self.assertEqual(res, testCase['output'])
    
    def test_Case2(self):
        testCase = self.testCases['2']
        res = self.obj.construct2DArray(testCase['original'],
                            testCase['m'], testCase['n'])
        
        self.assertIs(type(res), list)
        self.assertEqual(res, testCase['output'])

    def test_Case3(self):
        testCase = self.testCases['3']
        res = self.obj.construct2DArray(testCase['original'],
                            testCase['m'], testCase['n'])
        
        self.assertIs(type(res), list)
        self.assertEqual(res, testCase['output'])

    def test_empty_original_array(self):
        testCase = {'original': [], 'm': 0, 'n': 0, 'output': []}
        res = self.obj.construct2DArray(testCase['original'], 
                            testCase['m'], testCase['n'])
        
        self.assertIsInstance(res, list)
        self.assertEqual(res, testCase['output'])

    def test_zero_dimension(self):
        testCase = {'original': [1, 2, 3], 'm': 0, 'n': 0, 'output': []}
        res = self.obj.construct2DArray(testCase['original'], 
                            testCase['m'], testCase['n'])
        
        self.assertIsInstance(res, list)
        self.assertEqual(res, testCase['output'])


if __name__ == '__main__':
    unittest.main()