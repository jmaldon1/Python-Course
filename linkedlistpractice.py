class node:
	def __init__(self, data=None, prev, next):
		self.data = data
		self.next = next
		self.prev = prev

class linkedlist:
	def append(self, data):
		new_node = node(data, None, None)

		if self.head = None:
			self.head = self.tail = new_node
		else:
			new_node.prev = self.tail
			new_node.next = None
			self.tail.next = new_node
			self.tail = new_node

	def display(self):
		elems = []
		cur = self.head

		while cur.next != None:
			cur = cur.next
			elems.append(cur.data)
		print elems

	def erase(self, index):
		cur = self.head

		cur_idx = 0

		while True:
			last_node = cur
			cur = cur.next

			if cur_idx == index:
				last_node.next = cur.next
				return False
			else:
				cur_idx += 1



my_list = linkedlist()

my_list.append(1)
my_list.append(2)
my_list.append(3)

my_list.display()

my_list.erase(1)

my_list.display()
