class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        vector<int> p(1010);
        
        for (int i=0; i<(int)trips.size(); i++) {
            for (int j=trips[i][1]; j<trips[i][2]; j++) {
                p[j] += trips[i][0];
                if (p[j] > capacity) {
                    return false;
                }
            }
        }
        return true;
    }
};
