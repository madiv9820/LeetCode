#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
    public:
        vector<vector<int>> divideArray(vector<int>& nums, int k) {
            sort(nums.begin(), nums.end());
            vector<vector<int>> array;
            for(int index = 0; index < nums.size(); index += 3) {
                if(nums[index + 2] - nums[index] > k) return {};            
                array.push_back({nums[index], nums[index + 1], nums[index + 2]});
            }
            return array;
        }
};
int main() {
    int n, k; 
    do { cin >> n; if(n % 3 != 0) cout << "Should be multiple of 3" << endl; } while(n % 3 != 0); 
    vector<int> nums(n, 0);
    for(int index = 0; index < n; ++index) cin >> nums[index];
    cin >> k; Solution sol;
    cout << "Original Array: ";
    for(int index = 0; index < nums.size(); ++index) {
        if(index == 0) cout << '[';
        cout << nums[index];
        if(index == nums.size()-1) cout << ']';
        else cout << ',';
    }
    vector<vector<int>> array = sol.divideArray(nums, k);
    cout << "\nArray Divided with Max Difference = " << k << ": ";
    if(array.size() > 0) {
        for(int index1 = 0; index1< array.size(); ++index1) {
            if(index1 == 0) cout << '[';
            for(int index2 = 0; index2 < array[index1].size(); ++index2) {
                if(index2 == 0) cout << '[';
                if(index2 >= 0 && index2 < array[index1].size()-1)
                    cout << array[index1][index2] << ',';
                if(index2 == array.size()-1) cout << array[index1][index2] << "]";
            }
            if(index1 == array.size()-1) cout << ']';
            else cout << ',';
        }
    }
    else cout << "[]"; 
    cout << endl;
}