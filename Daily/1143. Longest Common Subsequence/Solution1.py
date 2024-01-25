from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
            Optimized Solution using Memoization
            Time Complexity: O(M*N)
            Space Complexity: O(M*N)
        '''
        '''
        text1_Size, text2_Size = len(text1) + 1, len(text2) + 1
        cache = [[-1] * text2_Size for _ in range(text1_Size)]
        
        @lru_cache(maxsize = None)
        def LCS(text1: str, text2: str) -> int:
            if len(text1) and len(text2):
                if cache[len(text1)][len(text2)] == -1:
                   if text1[0] == text2[0]: ans = 1 + LCS(text1[1:], text2[1:])
                   else: ans = max(LCS(text1, text2[1:]), LCS(text1[1:], text2)) 
                   cache[len(text1)][len(text2)] = ans
                return cache[len(text1)][len(text2)]
            return 0
        
        return LCS(text1, text2)
        '''
        @lru_cache(maxsize=None)
        def LCS(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            if text1[p1] == text2[p2]:
                return 1 + LCS(p1 + 1, p2 + 1)
            else:
                return max(LCS(p1, p2 + 1), LCS(p1 + 1, p2))
        return LCS(0, 0)

if __name__ == '__main__':
    text1, text2 = tuple(input().split()); sol = Solution()
    print('Longest Common Subsequence:', sol.longestCommonSubsequence(text1, text2))