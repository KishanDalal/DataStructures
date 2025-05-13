# LeetCode Problem: 225. Implement Stack using Queues
# Difficulty: Easy
# Link: https://leetcode.com/problems/implement-stack-using-queues/

# Problem Description:
# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the regular stack operations (push, top, pop, and empty).

# Implement the MyStack class:
# void push(int x) Pushes element x onto the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack without removing it.
# boolean empty() Returns true if the stack is empty, false otherwise.

# Notes:
# You must use only standard operations of a queue, which means only push to back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, the queue might not directly support all these operations. You may need to simulate some of them using only the available operations.
# You must use only two queues for your implementation.

class MyStack:
    def __init__(self):
        self.q1 = [] # Use a Python list as a queue
        self.q2 = [] # Use another Python list as a queue

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        # Move all elements except the last one from q1 to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        # The last element in q1 is the top of the stack
        result = self.q1.pop(0)
        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        return result

    def top(self) -> int:
        # Move all elements except the last one from q1 to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        # Peek the last element in q1
        result = self.q1[0]
        # Move the last element to q2
        self.q2.append(self.q1.pop(0))
        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        return result

    def empty(self) -> bool:
        # Return True if q1 is empty, otherwise False
        return len(self.q1) == 0

# Example Usage (you can uncomment this to test your implementation):
# myStack = MyStack()
# myStack.push(1)
# myStack.push(2)
# print(myStack.top()) # return 2
# print(myStack.pop()) # return 2
# print(myStack.empty()) # return False