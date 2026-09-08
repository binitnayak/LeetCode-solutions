from collections import defaultdict
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atMost(k):
            freq = defaultdict(int)
            left = 0
            distinct = 0
            ans = 0

            for right in range(len(nums)):

                if freq[nums[right]] == 0:
                    distinct += 1

                freq[nums[right]] += 1

                while distinct > k:
                    freq[nums[left]] -= 1

                    if freq[nums[left]] == 0:
                        distinct -= 1

                    left += 1

                ans += right - left + 1

            return ans

        return atMost(k) - atMost(k - 1)