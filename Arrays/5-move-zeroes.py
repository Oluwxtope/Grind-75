class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        p1 = 0
        p2 = 1
        while p2 < length:
            if nums[p1] == 0 and nums[p2] == 0:
                p2 += 1
            else:
                if nums[p1] == 0 and nums[p2] != 0:
                    temp = nums[p1]
                    nums[p1] = nums[p2]
                    nums[p2] = temp
                p1 += 1
                p2 += 1