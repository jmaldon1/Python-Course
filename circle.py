class Circle:
	def __init__(self, diameter):
		self.diameter = diameter

	#properties can be called like attributes
	@property
	def radius(self):
		return self.diameter / 2

	#Allows you to change the radius property
	#Cannot change a property without a setter
	@radius.setter
	def radius(self, radius):
		self.diameter = radius * 2

small = Circle(10)
print(small.diameter)
print(small.radius)
small.radius = 20
print(small.radius)
print(small.diameter)