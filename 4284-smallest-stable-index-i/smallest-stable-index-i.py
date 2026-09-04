class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)

        rightMin = [0] * n
        rightMin[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            rightMin[i] = min(nums[i], rightMin[i + 1])

        leftMax = nums[0]

        for i in range(n):
            leftMax = max(leftMax, nums[i])

            instability = leftMax - rightMin[i]

            if instability <= k:
                return i

        return -1