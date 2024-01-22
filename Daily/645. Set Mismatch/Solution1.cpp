#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
    public:
        vector<int> findErrorNums(vector<int>& nums) {
            /*
                Optimized Solution using Sorting
                Time Complexity = O(nlogn)
                Space Complexity = O(logn)
            */
            sort(nums.begin(), nums.end());
            int duplicate = -1, missing = 1; const int size = nums.size();
            vector<int> error(2);
            for(int index = 1; index < size; index++) {
                if(nums[index - 1] == nums[index]) duplicate = nums[index];
                else if(nums[index] > nums[index - 1] + 1) missing = nums[index - 1] + 1;
            }
            missing = (nums[size - 1] != size) ? size : missing;
            error[0] = duplicate; error[1] = missing;
            return error;
        }
};
int main() {
    int n; cin >> n; vector<int> nums(n); Solution sol;
    for(int index = 0; index < n; ++index) cin >> nums[index]; 
    vector<int> ans = sol.findErrorNums(nums);
    cout << "Duplicate Element = " << ans[0] 
        << " and Missing Element = " << ans[1] << endl;
}