import unittest
from Solution import Solution
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        self.testCase = {
            1: {'allowed': "cad", 'words': ["cc","acd","b","ba","bac","bad","ac","d"],
                'output': 4},
            2: {'allowed': "abc", 'words': ["a","b","c","ab","ac","bc","abc"],
                'output': 7},
            3: {'allowed': "ab", 'words': ["ad","bd","aaab","baa","badab"],
                'output': 2}
        }
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        try:
            test = self.testCase[1]
            res = self.obj.countConsistentStrings(test['allowed'], test['words'])
            self.assertEqual(res, test['output'])
        except Exception as e:
            raise e
    
    @timeout(0.5)
    def test_Case2(self):
        try:
            test = self.testCase[2]
            res = self.obj.countConsistentStrings(test['allowed'], test['words'])
            self.assertEqual(res, test['output'])
        except Exception as e:
            raise e
    
    @timeout(0.5)
    def test_Case3(self):
        try:
            test = self.testCase[3]
            res = self.obj.countConsistentStrings(test['allowed'], test['words'])
            self.assertEqual(res, test['output'])
        except Exception as e:
            raise e

if __name__ == '__main__':
    unittest.main()