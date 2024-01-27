class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 1000000007
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            prefix_sum = [0] * (k + 1)
            prefix_sum[0] = dp[i - 1][0]
            for j in range(1, k + 1):
                prefix_sum[j] = (prefix_sum[j - 1] + dp[i - 1][j]) % MOD
            for j in range(0, k + 1):
                if j - i >= 0:
                    dp[i][j] = (prefix_sum[j] - prefix_sum[j - i] + MOD) % MOD
                else:
                    dp[i][j] = prefix_sum[j]
        return dp[n][k]

if __name__ == '__main__':
    n, k = tuple([int(x) for x in input().split()]); sol = Solution()
    print('Number of K Inverse Pairs in an Array:', sol.kInversePairs(n,k))