import unittest
from typing import List
from Solution import PolyNode, Solution

def create_Polynomial(poly: List[List[int]]) -> 'PolyNode':
    start = end = None
    for coef, pow in poly:
        if start == None: start = end = PolyNode(coef, pow)
        else:
            end.next = PolyNode(coef, pow)
            end = end.next

    return start

def are_Polynomials_Equal(poly1: 'PolyNode', poly2: 'PolyNode') -> bool:
    poly_1, poly_2 = [], []

    while poly1: poly_1.append(poly1); poly1 = poly1.next
    while poly2: poly_2.append(poly2); poly2 = poly2.next

    if len(poly_1) != len(poly_2): return False

    for i in range(len(poly_1)):
        if poly_1[i] != poly_2[i]: return False

    return True

def is_Polynomial_In_Decreasing(poly: 'PolyNode') -> bool:
    if not poly: return True   
    prev = poly.power; poly = poly.next

    while poly:
        if poly.power > prev: return False
        prev = poly.power
        poly = poly.next

    return True

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()
        self.testCases = {
            1: {
                'poly1': [[1, 1]],
                'poly2': [[1, 0]],
                'output': [[1, 1], [1, 0]]
            },
            2: {
                'poly1': [[2, 2], [4, 1], [3, 0]],
                'poly2': [[3, 2], [-4, 1], [-1, 0]],
                'output': [[5, 2], [2, 0]]
            },
            3: {
                'poly1': [[1, 2]],
                'poly2': [[-1, 2]],
                'output': []
            }
        }

    def test_Case1(self):
        test = self.testCases[1]
        poly1 = create_Polynomial(test['poly1'])
        poly2 = create_Polynomial(test['poly2'])
        output = create_Polynomial(test['output'])

        res = self.obj.addPoly(poly1, poly2)
        msg = 'Polynomial should be in descreasing order of power'
        self.assertTrue(is_Polynomial_In_Decreasing(res), msg)
        self.assertEqual(are_Polynomials_Equal(res, output), True)

    def test_Case2(self):
        test = self.testCases[2]
        poly1 = create_Polynomial(test['poly1'])
        poly2 = create_Polynomial(test['poly2'])
        output = create_Polynomial(test['output'])

        res = self.obj.addPoly(poly1, poly2)
        msg = 'Polynomial should be in descreasing order of power'
        self.assertTrue(is_Polynomial_In_Decreasing(res), msg)
        self.assertEqual(are_Polynomials_Equal(res, output), True)
    
    def test_Case3(self):
        test = self.testCases[3]
        poly1 = create_Polynomial(test['poly1'])
        poly2 = create_Polynomial(test['poly2'])
        output = create_Polynomial(test['output'])

        res = self.obj.addPoly(poly1, poly2)
        msg = 'Polynomial should be in descreasing order of power'
        self.assertTrue(is_Polynomial_In_Decreasing(res), msg)
        self.assertEqual(are_Polynomials_Equal(res, output), True)

if __name__ == '__main__':
    unittest.main()