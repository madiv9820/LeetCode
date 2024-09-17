import unittest
from Solution import Solution
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        self.testCases = {
            1: {
                'regions': [["Earth","North America","South America"],
                            ["North America","United States","Canada"],
                            ["United States","New York","Boston"],
                            ["Canada","Ontario","Quebec"],
                            ["South America","Brazil"]],
                'region1': "Quebec",
                'region2': "New York",
                'output': "North America"
            },
            2: {
                'regions': [["Earth", "North America", "South America"],
                            ["North America", "United States", "Canada"],
                            ["United States", "New York", "Boston"],
                            ["Canada", "Ontario", "Quebec"],
                            ["South America", "Brazil"]],
                'region1': "Canada",
                'region2': "South America",
                'output': "Earth"
            }
        }
        return super().setUp()
    
    def test_Case1(self):
        try:
            case = self.testCases[1]
            res = self.obj.findSmallestRegion(case['regions'], case['region1'], case['region2'])
            self.assertEqual(res, case['output'])
        except Exception as e:
            raise e
        
    def test_Case2(self):
        try:
            case = self.testCases[2]
            res = self.obj.findSmallestRegion(case['regions'], case['region1'], case['region2'])
            self.assertEqual(res, case['output'])
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    unittest.main()