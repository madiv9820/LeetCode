import unittest
from timeout_decorator import timeout
from Solution import ListNode, Solution
from typing import List, Optional

class UnitTest(unittest.TestCase):
    def create_LL(self, heads: List[int]) -> Optional[ListNode]:
        head = tail = None
        for h in heads:
            if not head: head = tail = ListNode(h)
            else: tail.next = ListNode(h); tail = tail.next

        return head
    
    def compare_LL(self, 
                   head1: Optional[ListNode], 
                   head2: Optional[ListNode]) -> bool:
        while head1 and head2:
            if head1.val != head2.val: return False
            head1 = head1.next
            head2 = head2.next
        
        if head1 or head2: return False
        return True

    def setUp(self) -> None:
        self.obj = Solution()
        self.testCases = {
            1: {'nums': [1,2,3], 'head': [1,2,3,4,5], 'output': [4,5]},
            2: {'nums': [1], 'head': [1,2,1,2,1,2], 'output': [2,2,2]},
            3: {'nums': [5], 'head': [1,2,3,4], 'output': [1,2,3,4]},
            4: {'nums': [1,7,6,2,4], 'head': [3,7,1,8,1], 'output': [3,8]}
        }
        return super().setUp()
    
    def test_Case1(self):
        try:
            test = self.testCases[1]
            head = self.create_LL(test['head'])
            output = self.create_LL(test['output'])
            
            res = self.obj.modifiedList(test['nums'], head)
            self.assertIsInstance(res, ListNode)
            self.assertTrue(self.compare_LL(output, res), 
                                f'Correct Answer is {output}')
        except Exception as e:
            raise e
        
    def test_Case2(self):
        try:
            test = self.testCases[2]
            head = self.create_LL(test['head'])
            output = self.create_LL(test['output'])
            
            res = self.obj.modifiedList(test['nums'], head)
            self.assertIsInstance(res, ListNode)
            self.assertTrue(self.compare_LL(output, res), 
                                f'Correct Answer is {output}')
        except Exception as e:
            raise e
        
    def test_Case3(self):
        try:
            test = self.testCases[3]
            head = self.create_LL(test['head'])
            output = self.create_LL(test['output'])
            
            res = self.obj.modifiedList(test['nums'], head)
            self.assertIsInstance(res, ListNode)
            self.assertTrue(self.compare_LL(output, res), 
                                f'Correct Answer is {output}')
        except Exception as e:
            raise e

    def test_Case4(self):
        try:
            test = self.testCases[4]
            head = self.create_LL(test['head'])
            output = self.create_LL(test['output'])
            
            res = self.obj.modifiedList(test['nums'], head)
            self.assertIsInstance(res, ListNode)
            self.assertTrue(self.compare_LL(output, res), 
                                f'Correct Answer is {output}')
        except Exception as e:
            raise e
        

if __name__ == '__main__':
    unittest.main()