class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        string tmp;
        
        if (s == "") {
            return false;
        }
        
        tmp += s[0];
        for (int i=1; i<s.length(); i++) {
            //j=5まで
            for (int j=tmp.length(); j<s.length(); j+=tmp.length()) {
                if (tmp != s.substr(j, tmp.length())) {
                    tmp += s[i];
                    break;
                }
                if (j+tmp.length() >= s.length()) {
                    return true;
                }
            }
        }
        return false;
    }
};
