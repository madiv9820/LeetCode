import unittest
from timeout_decorator import timeout
from Solution import Solution

class UnitTest(unittest.TestCase):
    def check_Output(self, rolls, output, mean):
        if output == []: return True
        
        rolls += output
        return int(sum(rolls)/len(rolls)) == mean

    def setUp(self) -> None:
        self.obj = Solution()
        self.testCases = {
            1: {'rolls': [3,2,4,3], 'mean': 4, 'n': 2, 'output': [6,6]},
            2: {'rolls': [1,5,6], 'mean': 3, 'n': 4, 'output': [2,3,2,2]},
            3: {'rolls': [1,2,3,4], 'mean': 6, 'n': 4, 'output': []},
            4: {'rolls': [3,3,3,4,1,2,6,5,4,6,2,2,6,3,2,2,3,5,6,3,4,2,6,6], 'mean': 3, 'n': 33, 
                'output': [3,3,2,3,3,3,2,3,2,2,2,3,2,2,2,2,3,2,2,2,3,3,3,2,2,3,3,3,2,3,2,2,3]}
        }
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        try:
            test = self.testCases[1]
            res = self.obj.missingRolls(rolls = test['rolls'], mean = test['mean'], n = test['n'])
            self.assertIsInstance(res, list)
            self.assertTrue(self.check_Output(test['rolls'], res, test['mean']))
        except Exception as e:
            raise e
        
    @timeout(0.5)
    def test_Case2(self):
        try:
            test = self.testCases[2]
            res = self.obj.missingRolls(rolls = test['rolls'], mean = test['mean'], n = test['n'])
            self.assertIsInstance(res, list)
            self.assertTrue(self.check_Output(test['rolls'], res, test['mean']))
        except Exception as e:
            raise e
        
    @timeout(0.5)
    def test_Case3(self):
        try:
            test = self.testCases[3]
            res = self.obj.missingRolls(rolls = test['rolls'], mean = test['mean'], n = test['n'])
            self.assertIsInstance(res, list)
            self.assertTrue(self.check_Output(test['rolls'], res, test['mean']))
        except Exception as e:
            raise e
        
    @timeout(0.5)
    def test_Case4(self):
        try:
            test = self.testCases[3]
            res = self.obj.missingRolls(rolls = test['rolls'], mean = test['mean'], n = test['n'])
            self.assertIsInstance(res, list)
            self.assertTrue(self.check_Output(test['rolls'], res, test['mean']))
        except Exception as e:
            raise e
    
if __name__ == '__main__':
    unittest.main()