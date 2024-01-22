#include <iostream>
#include <vector>
using namespace std;
class Solution {
    public:
        vector<int> findErrorNums(vector<int>& nums) {
            /*
                Optimized Solution using Array or Vector
                Time Complexity = O(n)
                Space Complexity = O(n)
            */
            const int total_Elements = nums.size();
            int duplicate = -1, missing = -1;
            vector<int> frequency(total_Elements+1);
            for(const int& element: nums) frequency[element]++;
            for(int element = 1; element <= total_Elements; ++element) {
                if(frequency[element] > 1) duplicate = element;
                else if(frequency[element] == 0) missing = element;
            }
            return {duplicate, missing};
        }
};
int main() {
    int n; cin >> n; vector<int> nums(n); Solution sol;
    for(int index = 0; index < n; ++index) cin >> nums[index];
    vector<int> ans = sol.findErrorNums(nums);
    cout << "Duplicate Number = " << ans[0] 
        << " and Missing Number = " << ans[1] << endl;
}