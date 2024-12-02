class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int n = gain.size();
        int prefixsum[101] = {0};
        prefixsum[0]=0;
        int max = 0;
        for(int i = 1; i<n+1 ; i++){
            prefixsum[i]=prefixsum[i-1]+gain[i-1];
            if (prefixsum[i]>=max){
                max = prefixsum[i];
            }
        }
        return max;
    }
};