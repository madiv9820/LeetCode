#include <iostream>
#include <string>
#include <functional>
#include <vector>
using namespace std;
class Solution {
    public:
        int longestCommonSubsequence(string text1, string text2) {
            /*
                Optimized Solution using Recursion (Memoization)
                Time Complexity: O(M*N)
                Space Complexity: O(M*N)
            */
            vector<vector<int>> cache(text1.size()+1, vector<int>(text2.size()+1, -1));
            function<int(string, string)> LCS = [&](string text1, string text2) -> int {
                int text1_Size = text1.size(), text2_Size = text2.size();
                if(text1_Size && text2_Size) {
                    if(cache[text1_Size][text2_Size] == -1) {
                        int ans = 0;
                        if(text1[0] == text2[0]) ans = 1 + LCS(text1.substr(1), text2.substr(1));
                        else ans = max(LCS(text1.substr(1), text2), LCS(text1, text2.substr(1)));
                        cache[text1_Size][text2_Size] = ans;
                    }
                    return cache[text1_Size][text2_Size];
                }
                return 0;
            };
            return LCS(text1, text2);
        }
};
int main() {
    string text1, text2; Solution sol;
    cin >> text1 >> text2;
    cout << "Longest Common Subsequence: " << 
        sol.longestCommonSubsequence(text1, text2) << endl;
}