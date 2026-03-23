class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""
        
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            pal1 = expand_around_center(i, i)
            pal2 = expand_around_center(i, i + 1)
            for pal in [pal1, pal2]:
                if len(pal) > len(longest):
                    longest = pal
        
        return longest