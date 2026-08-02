class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = [0] * 26
        max_length = 0

        left = 0
        for right in range(len(s)):
            freqs[ord(s[right]) - ord("A")] += 1
            
            while ((right-left+1) - max(freqs) > k):
                freqs[ord(s[left]) - ord("A")] -= 1
                left += 1
            
            max_length = max(max_length, (right-left+1))
        
        return max_length