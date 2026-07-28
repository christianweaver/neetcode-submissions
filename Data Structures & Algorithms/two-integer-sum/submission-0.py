class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        for i, n in enumerate(nums):
            dict[n] = i
        
        for i, n in enumerate(nums):
            difference = target - nums[i]
            if difference in dict and dict[difference] != i:
                return [i, dict[difference]]

        return []