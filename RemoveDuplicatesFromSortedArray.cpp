class Solution {
    public:
        int removeDuplicates(vector<int>& nums) {
            int k=0;
            vector<int> temp;
            for(int i=0;i<nums.size()-1;i++){
                if(nums[i]==nums[i+1]){
                   continue;
                }else{
                   temp.push_back(nums[i]);
                }
            }
            temp.push_back(nums[nums.size()-1]);
            k=temp.size();
            for(int i=0;i<temp.size();i++){
                nums[i]=temp[i];
            }
            return k;
        }
    };