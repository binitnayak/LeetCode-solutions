class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxsum = nums[0]
        minsum = nums[0]
        max_answer = nums[0]

        for i in range(1, len(nums)):

            previous_max = maxsum
            previous_min = minsum

            maxsum = max(
                nums[i],
                previous_max * nums[i],
                previous_min * nums[i]
            )

            minsum = min(
                nums[i],
                previous_max * nums[i],
                previous_min * nums[i]
            )

            max_answer = max(max_answer, maxsum)

        return max_answer