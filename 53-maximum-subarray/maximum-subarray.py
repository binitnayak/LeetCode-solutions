class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        currentsum=nums[0]
        maxsum=nums[0]
        for i in range (1,len(nums)):
           currentsum=max(nums[i],currentsum+nums[i])
           maxsum=max(currentsum,maxsum)
        return maxsum