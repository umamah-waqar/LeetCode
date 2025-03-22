#include <algorithm>
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
       int j,k=0;
       vector<int> temp;
       for(int i=0;i<nums.size();i++){
        if(nums[i]==val){
            continue;
        }else{
            temp.push_back(nums[i]);
        }
       }
       k=temp.size();
       for(int i=0;i<temp.size();i++){
            nums[i]=temp[i];
       }
       return k;
    }
};