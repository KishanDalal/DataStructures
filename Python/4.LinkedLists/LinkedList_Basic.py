
class Node:
    def __init__(self, data):
        self.data = data  # The value stored in the node
        self.next = None  # Pointer to the next node (initially None)
class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty, so the head points to None

    # Method to add a new node at the beginning of the list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Method to add a new node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Method to print all the elements in the list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example of using the LinkedList class:
my_linked_list = LinkedList()

# Add elements to the end
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

# Add an element to the beginning
my_linked_list.prepend(0)

# Print the list
my_linked_list.print_list() # Output: 0 -> 1 -> 2 -> 3 -> None