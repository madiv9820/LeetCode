from typing import List
import sys

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        '''
            Optimized Solution
            Time Complexity = O(n)
            Space Complexity = O(n)
        '''
        SIZE,MOD,sum = len(arr),1000000007,0
        stack,left,right = [],[0]*SIZE,[SIZE]*SIZE
        for current_Index in range(SIZE):
            while len(stack) != 0 and arr[current_Index] < arr[stack[-1]]:
                right[stack[-1]] = current_Index
                stack.pop()
            left[current_Index] = stack[-1] if len(stack) != 0 else -1
            stack.append(current_Index)
        
        for current_Index in range(SIZE):
            sum = (sum + ((current_Index-left[current_Index]) * (right[current_Index] - current_Index) % MOD) * arr[current_Index] % MOD) % MOD

        return sum % MOD
        
if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    sol = Solution()
    ans = sol.sumSubarrayMins(arr)
    print(ans)