class Node:
    def __init__(self, value):
        self.value = value  # Stock price for the week
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list

    def append(self, value):
        # Add a new node to the end of the list
        new_node = Node(value)
        if not self.head:
            self.head = new_node  # If the list is empty, set the head to the new node
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Link the new node to the end of the list

    def display(self):
        # Print the linked list values
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

def find_highest_stock_price (head):
	max_price = float('-inf') # Step 1
	current_node = head # Step 2
	while current_node is not None: #Loop runs only if there are a value in the node.
		if current_node.value > max.price: #Step 3a
			max_price = current_node.value #Step 3b
		current_node = current_node.next #Step 3c
	return max_price #Step 4

# Create a linked list with stock prices
stock_prices = LinkedList()
stock_prices.append(45)
stock_prices.append(67)
stock_prices.append(89)
stock_prices.append(34)
stock_prices.append(78)

# Display the linked list
print("Stock prices over the last 52 weeks:")
stock_prices.display()

# Find and display the 52-week high
highest_price = find_highest_stock_price(stock_prices.head)
print(f"The highest stock price in the last 52 weeks is: {highest_price}")
