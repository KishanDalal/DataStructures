# Two Sum
# Description:
# Given an array of integers `nums` and an integer `target`, return the indices
# of the two numbers such that they add up to `target`.
#
# Constraints:
# - You may assume that each input has exactly one solution.
# - You may not use the same element twice.
#
# Sample Input:
# nums = [2, 7, 11, 15]
# target = 9
#
# Sample Output:
# [0, 1]
#
# Explanation:
# nums[0] + nums[1] == 2 + 7 == 9

nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):
  for i in range(len(nums)):
    for z in range(i+1, len(nums)):
      if nums[i] + nums[z] == target:
        return [i, z]
  return []

# Better approach with Dictionary 
def twoSum(nums, target):
    num_map = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []


print(twoSum(nums, target))