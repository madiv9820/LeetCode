from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        '''
            Finding out the sum of n missing rolls
            Total No of Observations = (n missing observations + m observations of rolls)
            Mean = (Sum(m observations of rolls) + Sum(n missing observations)) / Total No of observations
            Sum(n missing observations) = Mean * Total No of observations - Sum(m observations of rolls)
        '''
        missing_Rolls_Sum = (len(rolls) + n) * mean - sum(rolls)
        '''
            Checking whether the missing sum is withing range or not
            since we have n missing observations, we can have n observations
            with value = 1, which will get us minimum sum = 1*n, or we can have
            n observations with value = 6, which will get us maximum sum = 6 * n 
        '''
        if n <= missing_Rolls_Sum <= 6*n:
            res = [1] * n
            missing_Rolls_Sum -= n

            while missing_Rolls_Sum > 0:
                for i in range(n):
                    '''
                        For the balance values in res, use
                        res[i] -= 1; missing_Rolls_Sum -= 1
                    '''
                    # This will provide a skewed res, try to
                    # make initial position as max as it can
                    add = min(6-res[i], missing_Rolls_Sum)
                    res[i] += add; missing_Rolls_Sum -= add
                    if missing_Rolls_Sum == 0: break

            return res      # Returning the values
        
        '''
            If missing rolls sum does not lie in the range,
            we can return an empty array/list
        '''
        return []