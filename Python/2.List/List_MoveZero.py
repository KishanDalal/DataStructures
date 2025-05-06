# LeetCode Problem: 283. Move Zeroes
# Difficulty: Easy
# Link: https://leetcode.com/problems/move-zeroes/

# Problem Description:
# Given an array nums, move all the zeroes to the end of it while maintaining the relative
# order of the non-zero elements.
# You must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Constraints:
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4

# Your Task:
# Write a Python function called 'moveZeroes' that takes a list of integers 'nums' as input
# and modifies it in-place to move all zeroes to the end while preserving the order of
# the non-zero elements.

# Solution Approach (Hint - use two pointers):
# One pointer can track the position to place the next non-zero element, and another can iterate
# through the array. When a non-zero element is encountered, move it to the tracked position.

# Your Python function should look like this:
# def moveZeroes(nums: list[int]) -> None:

def moveZeroes(num: list[int]) -> None:
  if len(num) == 0:
    return None
  
  slow = 0 

  for fast in range(len(num)):
    if num[fast] != 0:
      num[slow], num[fast] = num[fast], num[slow]
      slow+=1

nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums) 