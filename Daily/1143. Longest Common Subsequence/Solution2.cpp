#include <iostream>
#include <string>
#include <functional>
#include <vector>
using namespace std;
class Solution {
    public:
        int longestCommonSubsequence(string text1, string text2) {
            /*
                Optimized Solution using Dynamic Programming
                Time Complexity: O(M*N)
                Space Complexity: O(M*N)
            */
            int text1_Size = text1.size(), text2_Size = text2.size();
            vector<vector<int>> cache(text1_Size+1,vector<int>(text2_Size+1,0));
            for(int index1 = 1; index1 <= text1_Size; ++index1) {
                for(int index2 = 1; index2 <= text2_Size; ++index2) {
                    if(text1[text1_Size-index1] == text2[text2_Size-index2])
                        cache[index1][index2] = 1 + cache[index1-1][index2-1];
                    else
                        cache[index1][index2] = max(cache[index1][index2-1], cache[index1-1][index2]);
                }
            }
            return cache[text1_Size][text2_Size];
        }
};
int main() {
    string text1, text2; Solution sol;
    cin >> text1 >> text2;
    cout << "Longest Common Subsequence: " << 
        sol.longestCommonSubsequence(text1, text2) << endl;
}