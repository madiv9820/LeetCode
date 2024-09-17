from typing import List

class Solution:
    def construct2DArray(self, 
                            original: List[int],
                            m: int,
                            n: int) -> List[List[int]]:
        '''
        # Getting total no of elements
        total_Elements = len(original)

        # Base Case
        if m * n != total_Elements: return []
        
        # 2D array
        res = [[-1] * n for _ in range(m)] 
        index = 0

        # Updating the elements in res
        for i in range(m):
            for j in range(n):
                res[i][j] = original[index]
                index += 1

        return res  # Returning 2D array
        '''
        # Creating 2D array in single line
        return ([original[(i * n): ((i+1) * n)] for i in range(m)]
                    if m*n == len(original) else [])