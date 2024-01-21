#include <iostream>
#include <vector>
using namespace std;
class Solution {
    public:
        int rob(vector<int>& nums) {
            /*
                Optimized Solution (Dynamic Programming)
                Time Complexity = O(n)
                Space Complexity = O(n)
            */
            int size = nums.size(); vector<int> cache(size + 1, 0); 
            cache[size-1] = nums[size-1];
            for(int index = size - 2; index >= 0; --index) 
                cache[index] = max(nums[index] + cache[index + 2], cache[index + 1]);
            return cache[0];
        }
};
int main() {
    int n; cin >> n; vector<int> nums(n,0); Solution sol;
    for(int index = 0; index < n; ++index) cin >> nums[index];
    cout << sol.rob(nums) << endl;
}