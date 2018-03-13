# Using dictionary

# While we iterate and insert the numbers into the dictionary, we look back to check if the current number's complement
# already exists in the dictionary. If it exists, return the solution.


class Solution:
    def twoSum(self, nums, target):
        lookup = {}
        for index, number in enumerate(nums):
            if target - number in lookup:
                return lookup[target - number], index
            else:
                lookup[number] = index

Solution().twoSum([2, 7, 8], 15)
