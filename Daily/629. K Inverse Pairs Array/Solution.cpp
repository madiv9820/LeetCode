#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int kInversePairs(int n, int k) {
        const int MOD = 1000000007;
        vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));
        dp[0][0] = 1;
        for (int i = 1; i <= n; ++i)
            for (int j = 0; j <= k; ++j)
                for (int m = 0; m <= std::min(j, i - 1); ++m)
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - m]) % MOD;
        return dp[n][k];
    }
};
int main() {
    int n, k; Solution sol;
    cin >> n >> k;
    cout << "Number of K Inverse Pairs in an Array: " << sol.kInversePairs(n, k) << endl;
}