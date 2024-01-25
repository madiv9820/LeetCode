#include <iostream>
#include <string>
using namespace std;
class Solution {
    public:
        int longestCommonSubsequence(string text1, string text2) {
            /*
                Unoptimized Solution using Recursion
                Time Complexity: O(2^(N+M))
                Space Complexity: O(N+M) 
            */
            if(text1.size() == 0 || text2.size() == 0) return 0;
            if(text1[0] == text2[0]) 
                return 1+longestCommonSubsequence(text1.substr(1), text2.substr(2));
            int case1 = longestCommonSubsequence(text1.substr(1), text2);
            int case2 = longestCommonSubsequence(text1, text2.substr(1));
            return max(case1, case2);
        }
};
int main() {
    string text1, text2; Solution sol;
    cin >> text1 >> text2;
    cout << "Longest Common Subsequence: " << 
        sol.longestCommonSubsequence(text1, text2) << endl;
}