# LeetCode Problem: 26. Remove Duplicates from Sorted Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Problem Description:
# Given a sorted array nums, remove the duplicates in-place such that each element appears
# only once and returns the new length of the array.
# Do not allocate extra space for another array; you must do this by modifying the input array
# in-place with O(1) extra memory.

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

# Your Task:
# Write a Python function called 'removeDuplicates' that takes a sorted list of integers 'nums'
# as input, modifies it in-place to remove duplicates, and returns the new length of the array
# after removing duplicates.

# Solution Approach (Hint - use two pointers):
# One pointer can iterate through the array, and another pointer can keep track of the position
# to place the next unique element.

# Your Python function should look like this:
# def removeDuplicates(nums: list[int]) -> int:

def removeDuplicates(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    slow = 0
    # Iterate through the array with the fast pointer
    for fast in range(1, len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]

    # Return the length of the unique elements
    return slow + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))  # Output: 5
print(nums[:5])  # Output: [0, 1, 2, 3, 4]
