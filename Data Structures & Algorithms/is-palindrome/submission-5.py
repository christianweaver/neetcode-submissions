class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            while left < right and not self.isAlphaNum(s[left]):
                left += 1
            while left < right and not self.isAlphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        
        return True

    def isAlphaNum(self, c):
        if (ord('A') <= ord(c) <= ord('Z')):
            return True
        if (ord('a') <= ord(c) <= ord('z')):
            return True
        if (ord('0') <= ord(c) <= ord('9')):
            return True
        return False
        