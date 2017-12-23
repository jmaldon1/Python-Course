import random

#Super class 
class Character:
	def __init__(self, name, **kwargs):
		self.name = name

		for key, value in kwargs.items():
			setattr(self, key, value)

#Thief Inherates the Character class
class Thief(Character):
	#Has an Attribute of 'sneaky'
	sneaky = True

	#Must override the __init__ method in the Characters class here in the Thief class
	def __init__(self, name, sneaky=True, **kwargs):
		#super() will pass the arguments to the __init__ method in super class
		super().__init__(name, **kwargs)
		self.sneaky = sneaky

	#Has a method(function inside a class) named pickpocket with the argument 'self'
	#'self' is required as an argument in a method
	def pickpocket(self):
		#If sneaky is set to True, pickpocket method will choose a random number between 1 and 0
			return self.sneaky and bool(random.randint(0,1))

	#A method with an argument besides 'self'
	def hide(self, light_level):
		#will return True if sneaky = true AND light_level < 10
		return self.sneaky and light_level < 10