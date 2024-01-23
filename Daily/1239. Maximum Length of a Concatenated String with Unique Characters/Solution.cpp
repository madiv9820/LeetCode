#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int maxLength(vector<string>& arr) {
        int result = 0;
        vector<string> validSubsequences;
        backtrack(arr, 0, "", validSubsequences, result);
        return result;
    }

private:
    void backtrack(const vector<string>& arr, int index, string current, vector<string>& validSubsequences, int& result) {
        unordered_set<char> charSet(current.begin(), current.end());

        // Check if the current subsequence has unique characters
        if (charSet.size() == current.size()) {
            // Update the result with the maximum length
            result = max(result, static_cast<int>(current.size()));
        } else {
            // If not, the current subsequence is invalid, so return without exploring further
            return;
        }

        // Explore subsequences with the current string included
        for (int i = index; i < arr.size(); ++i) {
            backtrack(arr, i + 1, current + arr[i], validSubsequences, result);
        }
    }
};

int main() {
    Solution sol;

    // Example 1
    vector<string> arr1 = {"un", "iq", "ue"};
    cout << "Example 1: " << sol.maxLength(arr1) << endl;

    // Example 2
    vector<string> arr2 = {"cha", "r", "act", "ers"};
    cout << "Example 2: " << sol.maxLength(arr2) << endl;

    // Example 3
    vector<string> arr3 = {"abcdefghijklmnopqrstuvwxyz"};
    cout << "Example 3: " << sol.maxLength(arr3) << endl;

    return 0;
}
