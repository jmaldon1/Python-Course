import random

#Creates an object named Thief
class Thief:
	#Has an Attribute of 'sneaky'
	sneaky = True

	#Python will run __init__ method automatically when class is called
	#Lets us control how the Class is initialized(created)
	#Kwargs are Key Word Arguments
	def __init__(self, name, sneaky=True, **kwargs):
		self.name = name
		self.sneaky = sneaky

		#Allows the user to input any key-value pairs they want
		#Example: Thief("Josh", sneaky = False, scar = None, favorite_weapon = "wit") 
		for key, value in kwargs.items():
			#Turns the each key-value pair into an attribute
			setattr(self, key, value)

	#Has a method(function inside a class) named pickpocket with the argument 'self'
	#'self' is required as an argument in a method
	def pickpocket(self):
		#If sneaky is set to True, pickpocket method will choose a random number between 1 and 0
			return self.sneaky and bool(random.randint(0,1))

	#A method with an argument besides 'self'
	def hide(self, light_level):
		#will return True if sneaky = true AND light_level < 10
		return self.sneaky and light_level < 10