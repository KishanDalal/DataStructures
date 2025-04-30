# Given an array nums, move all the zeroes to the end of it while maintaining
# the relative order of the non-zero elements. You must do this in-place
# without making a copy of the array.

#Input: nums = [0, 1, 0, 3, 12]
#Output: [1, 3, 12, 0, 0]

nums = [0, 0, 1]

def moveZeros(nums):
  index = 0
  
  for i in range(len(nums)):
    if nums[i] != 0:
      nums[index] = nums[i]
      index+=1
      
  for i in range(index, len(nums)):
    nums[i] = 0

  return nums  


print(moveZeros(nums))