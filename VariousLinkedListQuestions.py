class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def pushToFront(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def length(self):
		cur = self.head
		total = 0
		while cur != None:
			cur = cur.next
			total += 1
		return total

	def pushAfterIndex(self, index, data):
		new_node = Node(data)

		cur = self.head
		temp = cur

		idx = 0

		if index > self.length():
			print("Index out of range")
			return 
		elif self.length() == 0:
			self.pushToFront(data)
			return

		while index != idx:
			idx += 1

			temp = cur.next
			cur = cur.next
		temp = temp.next
		cur.next = new_node
		cur.next.next = temp

	def pushToEnd(self, data):
		new_node = Node(data)

		cur = self.head

		while cur.next != None:
			cur = cur.next

		cur.next = new_node
		cur.next.next = None

	def deleteAtPos(self, index):
		temp = self.head
		cur = self.head

		idx = 0

		if index == 0:
			self.head = temp.next
			temp = None
			return
		elif index > self.length():
			print("Index is out of range")
			return


		while idx != (index-1):
			cur = cur.next
			idx += 1

		cur.next = cur.next.next

	def reverse(self):
		prev = None
		cur = self.head
		
		while cur != None:
			next = cur.next
			cur.next = prev
			prev = cur
			cur = next
		self.head = prev

	def rearrange(self):
		slow = self.head 
		fast = slow.next

		while fast != None and fast.next != None:
			slow = slow.next
			fast = fast.next.next

		if self.length() == 1:
			return self.head

		secondhalf = slow.next
		slow.next = None
		firsthalf = self.head
		self.head = secondhalf
		self.reverse()

		
		secondhalf = self.head
		cur1 = firsthalf
		next1 = cur1.next

		cur2 = secondhalf
		next2 = secondhalf.next

		self.head = cur1

		while next1 != None and next2 != None:
			cur2.next = None
			cur1.next = cur2
			cur1 = cur1.next
			cur1.next = next1
			next1 = next1.next
			cur1 = cur1.next
			cur2 = next2
			next2 = next2.next
		if (self.length()) %2 == 0:
			cur2.next = next1
		cur1.next=cur2

	def zigzag(self):
		temp = Node(0)
		temp.next = self.head
		prev = temp
		ptr1 = prev.next


		flag = True #Flag = True means we are looking for A < B

		while prev.next != None and prev.next.next != None:
			if flag: #change A < B
				if ptr1.data > ptr1.next.data:
					ptr1 = prev.next
					ptr2 = prev.next.next

					prev.next = ptr2
					ptr1.next = ptr2.next
					ptr2.next = ptr1
					prev = prev.next
					flag = False
				else:
					prev = prev.next
					ptr1 = ptr1.next
					ptr2 = ptr2.next
					flag = False
			else: #change A > B
				if ptr1.data < ptr1.next.data:
					ptr1 = prev.next
					ptr2 = prev.next.next

					prev.next = ptr2
					ptr1.next = ptr2.next
					ptr2.next = ptr1
					prev = prev.next
					flag = True
				else:
					prev = prev.next
					ptr1 = ptr1.next
					ptr2 = ptr2.next
					flag = True
		self.head = temp.next

	def moveAllOccurancesToEnd(self, k):
		last = self.head
		cur = self.head
		prev = Node(0)
		prev.next = self.head
		
		while last.next != None:
			last = last.next
		temp = last


		while cur != temp:
			if cur.data == k:
				prev.next = cur.next
				cur.next = None
				last.next = cur
				last = last.next
				if cur == self.head:
					self.head = prev.next
				cur = prev

			prev = cur
			cur = cur.next

			
		
	def display(self):
		cur = self.head

		while cur != None:
			print(cur.data)
			cur = cur.next
		print("length: {}".format(self.length()))

ll = LinkedList()


ll.pushToFront(10)
ll.pushToFront(3)
ll.pushToFront(6)
ll.pushToFront(7)
ll.pushToFront(6)
ll.pushToFront(6)





ll.display()

#ll.pushAfterIndex(1,7)

#ll.display()

#ll.pushToEnd(9)

#ll.display()

#ll.deleteAtPos(2)

#ll.display()

#ll.rearrange()

ll.moveAllOccurancesToEnd(6)

ll.display()

