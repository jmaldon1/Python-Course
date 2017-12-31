import random

#allows you to choose a number of sides on a die
#will give you a random number between the 1 and the # of sides
#if you pass in value, the pick will not be random, but instead just return the value you set
class Die:
	def __init__(self, sides =2, value =0):
		if not sides >= 2:
			raise ValueError("Must have at least 2 sides")
		if not isinstance(sides, int):
			raise ValueError("Sides must be a whole number")
		if not isinstance(value, int):
			raise ValueError("Value must be a whole number")
		self.value = value or random.randint(1, sides)

	def __int__(self):
		return self.value

	def __eq__(self, other):
		return int(self) == other

	def __ne__(self, other):
		return int(self) != other

	def __gt__(self, other):
		return int(self) > other

	def __lt__(self, other):
		return int(self) < other

	def __ge__(self, other):
		return int(self) > other or int(self) == other

	def __le__(self, other):
		return int(self) < other or int(self) == other

	def __add__(self, other):
		return int(self) + other

	def __radd__(self, other):
		return int(self) + other

	def __repr__(self):
		return str(self.value)

#rolls a 6 sided die(most common die so we give it its own class)
class D6(Die):
	def __init__(self, value = 0):
		super().__init__(sides = 6, value = value)

