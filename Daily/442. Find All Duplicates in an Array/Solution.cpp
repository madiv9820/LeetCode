#include <iostream>
#include <vector>
#include <functional>
#include <unordered_map>
using namespace std;
class Solution {
    public:
        vector<int> findDuplicates(vector<int>& nums) {
            vector<int> duplicates; unordered_map<int,int> count_Freq;
            for(const int& x: nums) count_Freq[x]++;
            unordered_map<int,int>::iterator itr;
            for(itr = count_Freq.begin(); itr != count_Freq.end(); itr++)
                if(itr->second == 2) duplicates.emplace_back(itr->first);
            return duplicates;
        }
};
int main() {
    function<void(vector<int>)> printArray = [&](vector<int> array) {
        for(int index = 0; index < array.size(); ++index) {
            if(index == 0) cout << '[';
            cout << array[index];
            if(index == array.size()-1) cout << ']';
            else cout << ',';
        }
        cout << endl;
    };
    int n; cin >> n; vector<int> nums(n, 0); Solution sol;
    for(int index = 0; index < n; ++index) cin >> nums[index];
    cout << "Original Array: "; printArray(nums);
    vector<int> array = sol.findDuplicates(nums);
    cout << "Duplicates in Array: "; printArray(array);
}