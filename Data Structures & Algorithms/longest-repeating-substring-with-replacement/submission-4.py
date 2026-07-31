class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alph = [0] * 26
        max_length = 0

        left = right = 0

        while right < len(s):
            alph[ord(s[right]) - ord("A")] += 1

            while (right-left+1) - max(alph) > k:
                alph[ord(s[left]) - ord("A")] -= 1
                left += 1

            max_length = max(max_length, (right-left+1))
            right += 1

        return max_length
