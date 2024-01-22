from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        '''
            Optimized Solution Using Array or List
            Time Complexity: O(n)
            Space Complexity: O(n)
        '''
        total_Elements, duplicate, missing = len(nums), -1, -1
        frequency = [0] * (total_Elements + 1)
        for element in nums: frequency[element] += 1
        for element in range(1, total_Elements + 1):
            if frequency[element] > 1: duplicate = element
            elif frequency[element] == 0: missing = element
        return [duplicate, missing]

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]; sol = Solution()
    ans = sol.findErrorNums(nums)
    print('Duplicate Number =', ans[0], 'and Missing Number =', ans[1])