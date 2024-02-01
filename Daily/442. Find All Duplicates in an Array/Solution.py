from typing import List
from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
            duplicates, count_Freq = [], {}
            for num in nums: count_Freq[num] = count_Freq.get(num, 0) + 1
            for num, freq in count_Freq.items():
                if freq == 2: duplicates.append(num)
            return duplicates
        '''
        return [num for num, freq in Counter(nums).items() if freq == 2]
if __name__ == '__main__':
    nums = [int(x) for x in input().split()]; sol = Solution()
    print('Original Array:', nums)
    print('Duplicates in Array:', sol.findDuplicates(nums))