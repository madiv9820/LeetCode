from collections import defaultdict

class PolyNode:
    def __init__(self, x = 0, y = 0, next = None):
        self.coefficient = x
        self.power = y
        self.next = next

    def __eq__(self, value: 'PolyNode') -> bool:
        if not isinstance(value, PolyNode): return False
        return (value.power == self.power and 
                value.coefficient == self.coefficient)

class Solution:
    def addPoly(self, 
                    polyNode1: 'PolyNode',
                    polyNode2: 'PolyNode') -> 'PolyNode':
        '''
            Basically we are finding the sum of all the 
            coefficients correspoding to the power
            map[power] = sum of coefficient correspoding to power
            eg:- poly1 = 5(x^2) + 9(x) + 1
                 poly2 = 6(x^3) + 3(x^2) + 6(x) + 1
                 map[3] = 6
                 map[2] = 5+3 = 8
                 map[1] = 9+6 = 15
                 map[0] = 1+1 = 2
        '''
        # Creating map for all sum 
        # corresponding to power
        sum_of_powers = defaultdict(int)    

        # Getting sum of coefficients
        # for first polynomial
        while polyNode1:
            sum_of_powers[polyNode1.power] += polyNode1.coefficient
            polyNode1 = polyNode1.next

        # Getting sum of coefficients
        # for second polynomial
        while polyNode2:
            sum_of_powers[polyNode2.power] += polyNode2.coefficient
            polyNode2 = polyNode2.next
        
        # Sorting power and corresponding coefficient sum
        sum_of_powers = sorted(sum_of_powers.items(), reverse = True)
        start = end = None

        # Creating a new polynomial
        # with power and coefficient sum
        for pow, coef in sum_of_powers:
            if coef == 0: continue
            if start == None: start = end = PolyNode(coef, pow)
            else: end.next = PolyNode(coef, pow); end = end.next

        return start    # Return the polynomial