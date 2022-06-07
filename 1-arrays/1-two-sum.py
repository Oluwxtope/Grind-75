class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        for index, num in enumerate(nums):
            remainder = target - num
            if remainder in num_index:
                return [index, num_index[remainder]]
            else:
                num_index[num] = index