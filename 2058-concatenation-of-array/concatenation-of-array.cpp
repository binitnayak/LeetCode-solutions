class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size();
        vector<int>ans(2*n);
        for(int i=0; i< 2*n;i++){
        int index=i%n;
        int  value=nums[index];
        ans[i]=value;
        }
        return ans;

    }
};