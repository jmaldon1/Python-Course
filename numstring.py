class NumString:
	def __init__(self, value):
		self.value = str(value)

	def __str__(self):
		return self.value

	def __int__(self):
		return int(self.value)

	def __float__(self):
		return float(self.value)

	#EXAMPLE: NumString(5) + 5 = 10
	def __add__(self, other):
		if '.' in self.value:
			return float(self) + other
		return int(self) + other

	#If you reflect your addition, this method will reflect it again so the __add__ method can be used
	#EXAMPLE: 2 + NumString(5) becomes NumString(5) + 2 
	def __radd__(self, other):
		return self + other

	#will store a calculated self.value and therefore change the instance of NumString
	#EXAMPLE: NumString(25) += 5 will change Numstring(25) into Numstring(30)
	def __iadd__(self, other):
		self.value = self + other
		return self.value

