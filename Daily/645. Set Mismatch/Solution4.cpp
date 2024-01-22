#include <iostream>
#include <vector>
using namespace std;
class Solution {
    public:
        vector<int> findErrorNums(vector<int>& nums) {
            /*
                Optimized Solution using Array Modification
                Time Complexity = O(n)
                Space Complexity = O(1)
            */
            int duplicate = -1, missing = 1;
            const int total_Elements = nums.size();
            for(const int& element: nums)
                if(nums[abs(element) - 1] < 0) duplicate = abs(element);
                else nums[abs(element) - 1] *= -1;
            for(int element = 1; element < total_Elements; ++element)
                if(nums[element] > 0) missing = element + 1;
            return {duplicate, missing};
        }
};
int main() {
    int n; cin >> n; vector<int> nums(n); Solution sol;
    for(int index = 0; index < n; ++index) cin >> nums[index];
    vector<int> ans = sol.findErrorNums(nums);
    cout << "Duplicate Element = " << ans[0] 
        << " and Missing Element = " << ans[1] << endl;
}