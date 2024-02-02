from typing import List
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sequential_Numbers, digits = set(), '123456879'
        for length in range(len(str(low)), len(str(high)) + 1):
            for index in range(10 - length + 1):
                num = int(digits[index:index + length])
                if low <= num <= high: sequential_Numbers.add(num)
        return sorted(list(sequential_Numbers))
if __name__ == '__main__':
    low, high = (map(int, input().split())); sol = Solution()
    print('Sequential Numbers between', low, 'and', high, ':', sol.sequentialDigits(low, high))