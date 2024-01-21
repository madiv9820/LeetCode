from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            Optimized Solution (Memomization)
            Time Complexity = O(n)
            Space Complexity = O(n)
        '''
        cache = [-1]*len(nums)
        def find_Max_Amount(index: int = 0) -> int:
            if index >= len(nums): return 0
            if cache[index] == -1: 
                cache[index] = max(nums[index] + find_Max_Amount(index + 2), find_Max_Amount(index + 1))
            return cache[index]
        return find_Max_Amount()
if __name__ == '__main__':
    nums = [int(x) for x in input().split()]; sol = Solution()
    print(sol.rob(nums))