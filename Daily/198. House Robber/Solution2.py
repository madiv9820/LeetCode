from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            Optimized Solution (Dynamic Programmic)
            Time Complexity = O(n)
            Space Complexity = O(n)
        '''
        size = len(nums); cache = [0] * (size + 1)
        cache[size - 1] = nums[size - 1]
        for index in range(size - 2, -1, -1):
            cache[index] = max(nums[index] + cache[index + 2], cache[index + 1])
        return cache[0]
if __name__ == '__main__':
    nums = [int(x) for x in input().split()]; sol = Solution()
    print(sol.rob(nums))