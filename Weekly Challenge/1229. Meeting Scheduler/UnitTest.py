from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        self.testCases = {
            1: {
                'slots1': [[10,50],[60,120],[140,210]], 
                'slots2': [[0,15],[60,70]], 
                'duration': 8,
                'output': [60,68]
            },
            2: {
                'slots1': [[10,50],[60,120],[140,210]], 
                'slots2': [[0,15],[60,70]], 
                'duration': 12,
                'output': []
            },
            3: {
                'slots1': [[216397070,363167701],[98730764,158208909],[441003187,466254040],
                           [558239978,678368334],[683942980,717766451]],
                'slots2': [[50490609,222653186],[512711631,670791418],[730229023,802410205],
                           [812553104,891266775],[230032010,399152578]],
                'duration': 456085,
                'output': [98730764,99186849]
            }
        }
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        test = self.testCases[1]
        try:
            res = self.obj.minAvailableDuration(test['slots1'],
                                test['slots2'], test['duration'])
            self.assertEqual(res, test['output'])
        except Exception as e:
            raise e
    
    @timeout(0.5)
    def test_Case2(self):
        test = self.testCases[2]
        try:
            res = self.obj.minAvailableDuration(test['slots1'],
                                test['slots2'], test['duration'])
            self.assertEqual(res, test['output'])
        except Exception as e:
            raise e
        
    @timeout(0.5)
    def test_Case3(self):
        test = self.testCases[3]
        try:
            res = self.obj.minAvailableDuration(test['slots1'],
                                test['slots2'], test['duration'])
            self.assertEqual(res, test['output'])
        except Exception as e:
            raise e

if __name__ == '__main__':
    unittest.main()