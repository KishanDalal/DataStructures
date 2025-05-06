# LeetCode Problem: 136. Single Number
# Difficulty: Easy
# Link: https://leetcode.com/problems/single-number/

# Problem Description:
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

# Your Task:
# Write a Python function called 'singleNumber' that takes a list of integers 'nums' as input
# and returns the single number that appears only once.

# Solution Approach (Hint - you can use a dictionary to count occurrences):
# Iterate through the 'nums' list and store the frequency of each number in a dictionary.
# Then, iterate through the dictionary to find the number with a frequency of 1.

# Your Python function should look like this:
# def singleNumber(nums: list[int]) -> int:
#     counts = {} # Number -> Frequency
#     # Your code here
#     pass

nums = [4,1,2,1,2]

def singleNumber(nums: list[int]) -> int: 
  # Dic to count how many occurence each one has appeared. 
  counts = {}
  for val in nums: 
    # Lets check if it value exists in count already
    if (val in counts): 
      counts[val] += 1
    else:
      # Create a new key value pair with val being the key and value being occurence.
      counts[val] = 1 
  
  for key, value in counts.items():
        if value == 1:
            return key

print(singleNumber(nums))