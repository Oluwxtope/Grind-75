class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        majority_times = int(length/2)
        num_count = {}
        
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        
        for num in num_count:
            if num_count[num] > majority_times:
                return num