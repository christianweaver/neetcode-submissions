class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = set()

        for i,n in enumerate(nums):
            if(n == 0):
                zeros.add(i)
            else:
                product *= n
        
        res = [0] * len(nums)

        if(len(zeros) > 1):
            return res
        if(len(zeros) == 1):
            i = zeros.pop()
            res[i] = product
            return res

        for i,n in enumerate(nums):
            res[i] = int(product / nums[i])
        return res