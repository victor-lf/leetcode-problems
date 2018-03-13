# Brute force approach

# Loop through each element and find if there is another such that their sum equals the target.


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

Solution().twoSum([2, 7, 8], 15)
