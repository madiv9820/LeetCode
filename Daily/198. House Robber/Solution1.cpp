#include <iostream>
#include <vector>
#include <functional>
using namespace std;
class Solution {
    public:
        int rob(vector<int>& nums) {
            /*
                Optimized Solution (Memomization)
                Time Complexity = O(n)
                Space Complexity = O(n)
            */
            vector<int> cache(nums.size(), -1);
            function<int(int)> find_Max_Amount = [&](int index) {
                if(index >= nums.size()) return 0;
                if(cache[index] == -1) cache[index] = max(nums[index] + find_Max_Amount(index + 2), find_Max_Amount(index + 1));
                return cache[index];
            };
            return find_Max_Amount(0);
        }
};
int main() {
   int n; cin >> n;
   vector<int> nums(n, 0); for(int index = 0; index < n; ++index) cin >> nums[index];
   Solution sol; cout << sol.rob(nums) << endl; 
}