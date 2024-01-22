from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        '''
            Optimized Solution using Array Modification
            Time Complexity = O(n)
            Space Complexity = O(1)
        '''
        duplicate, missing = -1, 1
        for element in nums:
            if nums[abs(element) - 1] < 0: duplicate = abs(element)
            else: nums[abs(element) - 1] *= -1
        for element in range(1, len(nums)):
            if nums[element] > 0: missing = element + 1
        return [duplicate, missing]
    
if __name__ == '__main__':
    nums = [int(x) for x in input().split()]; sol = Solution()
    ans = sol.findErrorNums(nums)
    print('Duplicate Element =', ans[0], 'and Missing Element =', ans[1])