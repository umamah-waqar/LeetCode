#include <stack>
#include <string>
#include <unordered_map>

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        unordered_map<char, char> match = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };

        for (char c : s) {
            if (match.count(c)) { // if c is a closing bracket
                if (st.empty() || st.top() != match[c]) {
                    return false;
                }
                st.pop();
            } else { // if c is an opening bracket
                st.push(c);
            }
        }

        return st.empty();
    }
};