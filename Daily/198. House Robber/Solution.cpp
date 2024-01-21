#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;
class Solution {
    public:
        int rob(vector<int>& nums) {
            /*
                Unoptimized Solution using recursion
                T(n-0) = T(n-1) + T(n-2)
                T(n-1) = T(n-2) + T(n-3)
                T(n-2) = T(n-3) + T(n-4)
                ........................
                T(n-n) = 0
                Time Complexity = O(2^n)
                Space Complexity = O(n)
            */
            function<int(int)> find_Max_Amount = [&](int index) {
                if(index >= nums.size()) return 0;
                int choice1 = nums[index] + find_Max_Amount(index + 2);
                int choice2 = find_Max_Amount(index + 1);
                return max(choice1,choice2);
            };
            return find_Max_Amount(0);
        }
};
int main() {
    int n; cin >> n;
    vector<int> nums(n, 0); for(int index = 0; index < n; index++) cin >> nums[index];
    Solution sol; int ans = sol.rob(nums);
    cout << ans << endl;
}