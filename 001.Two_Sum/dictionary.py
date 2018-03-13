# Using dictionary

class Solution:
    def twoSum(self, nums, target):
        lookup = {}
        for index, number in enumerate(nums):
            if target - number in lookup:
                return lookup[target - number], index
            else:
                lookup[number] = index

Solution().twoSum([2, 7, 8], 15)
