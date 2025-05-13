class Stack:
    def __init__(self):
        self._items = []  # Use an underlying list to store the stack elements

    def push(self, item):
        """Adds an item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Removes and returns the item at the top of the stack.
        Raises an IndexError if the stack is empty."""
        if not self.is_empty():
            return self._items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        """Returns the item at the top of the stack without removing it.
        Returns None if the stack is empty."""
        if not self.is_empty():
            return self._items[-1]
        else:
            return None

    def is_empty(self):
        """Returns True if the stack is empty, False otherwise."""
        return len(self._items) == 0

    def size(self):
        """Returns the number of items in the stack."""
        return len(self._items)

# Example Usage:
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

print("Stack:", my_stack._items)  # Accessing the underlying list (for demonstration)

print("Top element (peek):", my_stack.peek())

popped_item = my_stack.pop()
print("Popped element:", popped_item)
print("Stack after pop:", my_stack._items)

print("Is stack empty?", my_stack.is_empty())
print("Size of stack:", my_stack.size())

my_stack.pop()
my_stack.pop()
print("Is stack empty now?", my_stack.is_empty())
