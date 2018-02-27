import copy

class FilledList(list):
	def __init__(self, count, value, *args, **kwargs):
		#ignore what was passed in because we want an empty list
		super().__init__()
		# the _ ignores the number that comes out of range
		for _ in range(count):
			#Append the value that was given
			#If you pass in multiple lists, without copy.copy,
			#if u changed one item a list, the item will change it for all lists
			self.append(copy.copy(value))