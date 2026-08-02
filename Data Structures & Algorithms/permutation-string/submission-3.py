class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq_s1 = [0] * 26
        freq_s2 = [0] * 26

        for i in range(len(s1)):
            freq_s1[ord(s1[i]) - ord("a")] += 1
            freq_s2[ord(s2[i]) - ord("a")] += 1

        if (freq_s1 == freq_s2):
            return True
        
        left = 0
        for i in range(len(s1), len(s2), 1):
            freq_s2[ord(s2[left]) - ord("a")] -= 1
            left += 1

            freq_s2[ord(s2[i]) - ord("a")] += 1

            if (freq_s1 == freq_s2):
                return True
        
        return False
        