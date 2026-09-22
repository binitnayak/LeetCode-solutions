class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""

        for center in range(len(s)):

           
            left = center
            right = center

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if right - left - 1 > len(answer):
                answer = s[left + 1:right]

           
            left = center
            right = center + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if right - left - 1 > len(answer):
                answer = s[left + 1:right]

        return answer