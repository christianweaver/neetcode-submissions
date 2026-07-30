class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        max_length = 1
        sett = set()
        left = 0
        right = 0
        

        while right < len(s):
            if s[right] not in sett:
                sett.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                sett.remove(s[left])
                left += 1
        
        return max_length

