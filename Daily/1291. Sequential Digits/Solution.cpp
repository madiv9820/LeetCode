#include <iostream>
#include <vector>
#include <functional>
#include <string>
#include <set>
using namespace std;
class Solution {
    public:
        vector<int> sequentialDigits(int low, int high) {
            set<int> sequential_Numbers; string digits = "123456789";
            for(int length = to_string(low).size(); length <= to_string(high).size(); ++length) {
                for(int index = 0; index <= 10 - length; ++index) {
                    string numStr = digits.substr(index, length);
                    int num = stoi(numStr);
                    if(num >= low && num <= high) sequential_Numbers.insert(num);
                }
            }
            return vector<int>(sequential_Numbers.begin(), sequential_Numbers.end());
        }
};
int main() {
    function<void(vector<int>)> printVector = [&](vector<int> array) -> void {
        cout << '[';
        for(int index = 0; index < array.size(); ++index) {
            cout << array[index];
            if(index < array.size()-1) cout << ',';
        }
        cout << ']' << endl;
    };
    int low, high; Solution sol; cin >> low >> high;
    vector<int> sequential_Numbers = sol.sequentialDigits(low, high);
    cout << "All Sequential Numbers between " << low << " and " << high << ": ";
    printVector(sequential_Numbers);
}