from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            Unoptimized Solution
            Time Complexity = O(2^n)
            Space Complexity = O(n)
        '''
        def find_Max_Amount(index: int = 0) -> int:
            if index >= len(nums): return 0
            return max(nums[index] + find_Max_Amount(index + 2), find_Max_Amount(index + 1))
        return find_Max_Amount()
if __name__ == '__main__':
    nums = [int(x) for x in input().split()]; sol = Solution()
    print(sol.rob(nums))