class Inventory:
	def __init__(self):
		self.slots = []

	def add(self, item):
		self.slots.append(item)

	#Magic method that checks the length of a list
	def __len__(self):
		return len(self.slots)

	#Magic method that checks if an item is in the list
	def __contains__(self, item):
		return item in self.slots

	def __iter__(self):
			#YIELD: allows you to send values out of the method and conitues through the method
			yield from self.slots