class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int p1= 0;
        int p2= 0;
       
        vector<int> merged(m+n);
        int i = 0; 

        while (m > 0 && n > 0) {
            if (nums1[p1] <= nums2[p2]) {
                merged[i++] = nums1[p1];
                p1++;
                m--;
            } else {
                merged[i++] = nums2[p2];
                p2++;
                n--;
            }
        }
        
        while (m > 0) {
            merged[i++] = nums1[p1];
            p1++;
            m--;
        }
  
        while (n > 0) {
            merged[i++] =nums2[p2];
            p2++;
            n--;
        }

        for (int j = 0; j < merged.size(); j++) {
            nums1[j] = merged[j];
        }
    }
};