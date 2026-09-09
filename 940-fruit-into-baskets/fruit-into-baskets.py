from collections import defaultdict

class Solution:
    def totalFruit(self, fruits):
        freq = defaultdict(int)

        left = 0
        distinct = 0
        ans = 0

        for right in range(len(fruits)):

           
            if freq[fruits[right]] == 0:
                distinct += 1

            freq[fruits[right]] += 1

            
            while distinct > 2:

                freq[fruits[left]] -= 1

                if freq[fruits[left]] == 0:
                    distinct -= 1

                left += 1

            
            ans = max(ans, right - left + 1)

        return ans