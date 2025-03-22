#include<algorithm>
using namespace std;
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count=0,mxm=0,idx;
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size()-1;i++){

            if(nums[i+1]==nums[i]){
                count++;
            }else{
                count=0;
            }
            if(count>mxm){
               idx=i;
            }
            mxm=max(mxm,count);
        }
        return nums[idx];
    }
};