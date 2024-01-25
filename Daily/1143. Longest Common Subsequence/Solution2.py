class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
            Optimized Solution using Dynamic Programming
            Time Complexity: O(M * N)
            Space Complexity: O(M * N)
        '''
        text1_Size, text2_Size = len(text1), len(text2)
        cache = [[0] * (text2_Size + 1) for _ in range(text1_Size + 1)]
        for index1 in range(1, text1_Size + 1):
            for index2 in range(1, text2_Size + 1):
                if text1[text1_Size - index1] == text2[text2_Size - index2]:
                    cache[index1][index2] = 1 + cache[index1 - 1][index2 - 1]
                else:
                    cache[index1][index2] = max(cache[index1][index2 - 1], cache[index1 - 1][index2])
        return cache[text1_Size][text2_Size]

if __name__ == '__main__':
    text1, text2 = tuple(input().split()); sol = Solution()
    print('Longest Common Subsequence:', sol.longestCommonSubsequence(text1, text2))