#Class that creates a node
class node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

#Class that creates the linked list
class linked_list:
	#Constructor that sets the head node to an empty node, users cannot see this node
	def __init__(self):
		self.head = node()

	#appends a new node onto the list, alows the user to pass in data
	def append(self, data):
		new_node = node(data)
		#current node = head node, always start at the beginning of the list
		cur = self.head
		#goes through the lists checking if the next node is NONE
		while cur.next != None:
			#if the next node is not equal to NONE, keep looping through the list 
			cur = cur.next
		#Once the last node is found, we create a new node
		cur.next = new_node

	#Gets the length of the list
	def length(self):
		cur = self.head
		total = 0
		while cur.next != None:
			total += 1
			cur = cur.next
		return total

	#Creates a visual representation of the linked list in the form of a python List
	def display(self):
		elems = []
		cur_node = self.head
		while cur_node.next != None:
			cur_node = cur_node.next
			#appends the data in each node into a list
			elems.append(cur_node.data)
		print(elems)

	#allows the user to retrieve any value in the list using an index
	def get(self, index):
		#If the index is larger than the length of the list, an error is thrown
		if index >= self.length():
			print("ERROR: 'Get' Index out of range")
			return None
		cur_idx = 0
		cur_node = self.head
		while True:
			cur_node = cur_node.next
			if cur_idx == index: 
				return cur_node.data
			else:
				cur_idx += 1

	#Allows the user to erase any item in the list using an index
	def erase(self, index):
		if index >= self.length():
			print("ERROR: 'Erase' Index out of range")
			return None
		cur_idx = 0
		cur_node = self.head
		while True:
			#sets last_node equal to current node
			last_node = cur_node
			#Then we set cur_node equal to the next node
			cur_node = cur_node.next
			if cur_idx == index:
				#deletes the current node by pointing the last node to the node after the current node
				last_node.next = cur_node.next
				return
			else:
				cur_idx += 1 


my_list = linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()

my_list.erase(1)

my_list.display()

