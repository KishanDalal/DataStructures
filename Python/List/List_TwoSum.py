# LeetCode Problem: 1. Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/

# Problem Description:
# Given an array of integers nums and an integer target, return indices of the two numbers
# such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]


# Your Task:
# Write a Python function called 'twoSum' that takes a list of integers 'nums' and an integer 'target'
# as input, and returns a list containing the indices of the two numbers that add up to the target.

# Solution Approach (Hint - you might consider using a dictionary/hash map):
# Iterate through the 'nums' list. For each number, check if the complement (target - number)
# exists in the rest of the list. To do this efficiently, you can store previously encountered
# numbers and their indices in a dictionary.

# Your Python function should look like this:
# def twoSum(nums: list[int], target: int) -> list[int]:

nums = [3, 3]
target = 6

def twoSum(nums: list[int], target: int) -> list[int]:
  seen = {}
  for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
      return [seen[complement], i]
    seen[num] = i 
  return []

print(twoSum(nums, target))