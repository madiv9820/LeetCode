from typing import List
from collections import Counter, defaultdict
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        '''
            Optimized Solution using Maps
            Time Complexity = O(n)
            Space Complexity = O(n)
        '''
        total_Elements, duplicate, missing = len(nums), -1, -1
        # frequency = dict(Counter(nums))
        frequency = defaultdict(int)
        for element in nums: frequency[element] += 1
        for element in range(1, total_Elements + 1):
            if frequency.get(element, 0) == 0: missing = element
            elif frequency[element] > 1: duplicate = element
        return [duplicate, missing]

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]; sol = Solution()
    ans = sol.findErrorNums(nums)
    print('Duplicate Element =', ans[0], 'and Missing Element =', ans[1])