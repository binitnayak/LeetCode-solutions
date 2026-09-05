class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        window_sum = 0
        max_sum = 0
        freq = {}

        for right in range(len(nums)):
            window_sum += nums[right]

            freq[nums[right]] = freq.get(nums[right], 0) + 1

            if right - left + 1 > k:
                x = nums[left]
                window_sum -= x

                freq[x] -= 1

                if freq[x] == 0:
                    del freq[x]

                left += 1

            if right - left + 1 == k:
                if len(freq) == k:
                    max_sum = max(max_sum, window_sum)

        return max_sum