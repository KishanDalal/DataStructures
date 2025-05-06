# LeetCode Problem: 242. Valid Anagram
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-anagram/

# Problem Description:
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.

# Your Task:
# Write a Python function called 'isAnagram' that takes two strings 's' and 't' as input
# and returns True if 't' is an anagram of 's', and False otherwise.

# Solution Approach (Hint - use dictionaries to count character frequencies):
# Create two dictionaries (or one and update/compare) to store the frequency of each character
# in both strings. If the character counts are the same for all characters, then they are anagrams.

# Your Python function should look like this:
# def isAnagram(s: str, t: str) -> bool:
#     # Your code here
#     pass

s = "anagram" 
t = "nagaram"

def isAnagram(s: str, t: str) -> bool:
  s_anagram = {}
  t_anagram = {}
  for i in s:
    if i in s_anagram:
      s_anagram[i] += 1
    else:
      s_anagram[i] = 1

  for i in t:
    if i in t_anagram:
      t_anagram[i] += 1
    else:
      t_anagram[i] = 1
  
  if(s_anagram == t_anagram):
    return True
  else:
    return False
  
print(isAnagram(s, t))