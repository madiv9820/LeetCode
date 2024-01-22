#include <iostream>
#include <vector>
using namespace std;
class Solution {
    public:
        vector<int> findErrorNums(vector<int>& nums) {
            /*
                Unoptimized Solution
                Time Complexity = O(n^2)
                Space Complexity = O(1)
            */
            vector<int> error(2);
            int number_Occured_Twice = -1, missing_Number = -1;
            const int total_Elements = nums.size();
            for(int current_Element = 1; current_Element <= total_Elements; current_Element++) {
                int count = 0;
                for(const int& element_In_Nums: nums)
                    if(element_In_Nums == current_Element) count++;
                if(count > 1) number_Occured_Twice = current_Element;
                else if(count == 0) missing_Number = current_Element;
                if(number_Occured_Twice != -1 && missing_Number != -1) break;
            }
            error[0] = number_Occured_Twice; error[1] = missing_Number;
            return error;
        }
};
int main() {
    int n; cin >> n; vector<int> nums(n); Solution sol;
    for(int index = 0; index < n; index++) cin >> nums[index];
    vector<int> ans = sol.findErrorNums(nums);
    cout << "Number that occured twice = " << ans[0] 
        << " and Missing number = " << ans[1] << endl;
}