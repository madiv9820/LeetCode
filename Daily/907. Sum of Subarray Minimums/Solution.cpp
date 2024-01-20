#include <iostream>
#include <vector>
#include <climits>
#define MOD 1000000007
using namespace std;

class Solution {
    public:
        /*
            Unoptimized Solution
            Time Complexity = O(n^3)
            Space Complexity = O(1)
        */
        int subArrayMins(vector<int>& arr) {
            int sum = 0, size = arr.size();
            for(int start_Index = 0; start_Index < size; start_Index++) {
                for(int end_Index = start_Index; end_Index < size; end_Index++) {
                    int min_Value = INT_MAX;
                    for(int current_Index = start_Index; current_Index <= end_Index; current_Index++)
                        min_Value = min(min_Value, arr[current_Index]);
                    sum = (sum + min_Value) % MOD;
                }
            }
            return sum % MOD;
        }
};

int main() {
    int n; cin >> n;
    vector<int> arr(n,0);
    for(int index = 0; index < n; index++) cin >> arr[index];
    Solution sol; int ans = sol.subArrayMins(arr);
    cout << ans << endl;
}