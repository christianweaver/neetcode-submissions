class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res, sol = [], []
        n = len(nums)

        def dfs(cur_sum, ind):
            if cur_sum == target:
                res.append(sol[:])
                return
            
            if cur_sum > target:
                return
            
            while ind < n:
                sol.append(nums[ind])
                dfs(cur_sum + nums[ind], ind)
                sol.pop()
                ind += 1
        
        dfs(0, 0)
        return res