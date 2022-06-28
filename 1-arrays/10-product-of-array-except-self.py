class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        length = len(nums)
        prefix = 1
        for i in range(length):
            res.append(prefix)
            prefix *= nums[i]
        postfix = 1
        for j in range(length - 1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
        return res