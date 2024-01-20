from typing import List
import sys

class Solution:
    def sumSubarrayMins(self, arr:List[int]) -> int:
        SIZE,MOD,sum = len(arr),1000000007,0
        for start_Index in range(SIZE):
            for end_Index in range(start_Index, SIZE):
                min_Value = sys.maxsize
                for current_Index in range(start_Index, end_Index+1): 
                    min_Value = min(min_Value, arr[current_Index])
                sum = (sum + min_Value) % MOD                   
        return sum % MOD
        
if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    sol = Solution()
    ans = sol.sumSubarrayMins(arr)
    print(ans)