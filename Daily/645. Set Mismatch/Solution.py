from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        error, total_Elements = [0,0], len(nums) + 1
        duplicate, missing = -1, -1
        for current_element in range(1, total_Elements):
            count = 0
            for element in nums: 
                if element == current_element: count += 1
            if count > 1: duplicate = current_element
            elif count == 0: missing = current_element
            if duplicate != -1 and missing != -1: break
        error[0], error[1] = duplicate, missing
        return error

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]; sol = Solution()
    ans = sol.findErrorNums(nums)
    print('Duplicate Element =', ans[0], 'and', 'Missing Element =', ans[1])