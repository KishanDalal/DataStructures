# LeetCode Problem: 206. Reverse Linked List
# Difficulty: Easy
# Link: https://leetcode.com/problems/reverse-linked-list/

# Problem Description:
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

# Constraints:
# The number of nodes in the list is in the range [0, 5000].
# -5000 <= Node.val <= 5000

# Your Task:
# Write a Python function called 'reverseList' that takes the head of a singly linked list
# as input and returns the head of the reversed linked list.

# Definition for singly-linked list:
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# Your Python function should look like this:
from typing import Optional

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
	prev = None
	current = head
	while current:
		next_node = current.next  # Store the next node
		current.next = prev       # Reverse the link
		prev = current            # Move prev to current
		current = next_node       # Move to the next node
	return prev


