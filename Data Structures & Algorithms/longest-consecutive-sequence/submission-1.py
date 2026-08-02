class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_freq = 0

        for num in num_set:
            if (num - 1) not in num_set:
                freq = 0
                while num in num_set:
                    freq += 1
                    num += 1
                max_freq = max(max_freq, freq)
        
        return max_freq
                