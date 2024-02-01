from typing import List
class Solution:
    def divideArray(self, nums: List[int], k: int):
        array = []; nums.sort()
        for index in range(0, len(nums), 3):
            if nums[index + 2] - nums[index] > k: return []
            array.append([nums[x] for x in range(index, index+3)])
        return array
if __name__ == '__main__':
    nums = [int(x) for x in input().split()]; k = int(input()); 
    print('Original Array:', nums); sol = Solution()
    print('Array with Max Difference =', k, ':', sol.divideArray(nums, k))