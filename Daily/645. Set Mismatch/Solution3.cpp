#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
class Solution {
    public:
        vector<int> findErrorNums(vector<int>& nums) {
            /*
                Optimized Solution using Maps
                Time Complexity = O(n)
                Space Complexity = O(n)
            */
            unordered_map<int, int> frequency;
            int duplicate = -1, missing = -1; const int total_Elements = nums.size();
            for(const int& element: nums) frequency[element]++;
            for(int element = 1; element <= total_Elements; ++element)
                if(frequency.find(element) == frequency.end()) missing = element;
                else if(frequency[element] > 1) duplicate = element;
            return {duplicate, missing};
        }
};
int main() {
    int n; cin >> n; vector<int> nums(n);
    for(int index = 0; index < n; index++) cin >> nums[index];
    Solution sol; vector<int> ans = sol.findErrorNums(nums);
    cout << "Duplicate Number = " << ans[0] 
        << " and Missing Number = " << ans[1] << endl;
}