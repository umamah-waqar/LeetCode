class Solution {
    public:
        void rotate(vector<int>& nums, int k) {
            int start=0+(k-1);
            int j=start;
            vector<int> copy=nums;
            for(int i=0;i<copy.size();i++){
                nums[((j+1)%copy.size())]=copy[i];
                j++;
            }
        }
    };