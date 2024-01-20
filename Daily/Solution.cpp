#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class Solution {
    public:
        /*
            Optimized Solution
            Time Complexity = O(n)
            Space Complexity = O(n)
        */
        int sumSubarrayMins(vector<int>& arr) {
            const int MOD = 1000000007, size = arr.size();
            long long int sum = 0; stack<int> st; vector<int> left(size), right(size,size);
            for(int index = 0; index < size; ++index) {
                while(!st.empty() && arr[index] < arr[st.top()]) {
                    int popped_Index = st.top(); st.pop();
                    right[popped_Index] = index;
                }
                left[index] = (st.empty()) ? -1:st.top();
                st.push(index);
            }
            for(int index = 0; index < size; ++index)
                sum = (sum + (long long int)(index-left[index])*(right[index]-index)%MOD * arr[index] % MOD) % MOD;
            return sum % MOD;
        }
};

int main() {
    int n; cin >> n;
    vector<int> arr(n,0);
    for(int index = 0; index < n; index++) cin >> arr[index];
    Solution sol; int ans = sol.sumSubarrayMins(arr);
    cout << ans << endl;
}