from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        '''
            Optimized Solution using Sorting
            Time Complexity = O(nlogn)
            Space Complexity = O(logn)
        '''
        duplicate, missing, size = -1, 1, len(nums)
        nums.sort()
        for index in range(1, size):
            if nums[index] == nums[index - 1]: duplicate = nums[index]
            if nums[index] != nums[index - 1] + 1: missing = nums[index - 1] + 1
        missing = size if nums[size - 1] != size else missing
        return [duplicate, missing]

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]; sol = Solution()
    ans = sol.findErrorNums(nums)
    print('Duplicate Number =', ans[0], 'Missing Number =', ans[1])