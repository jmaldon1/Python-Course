class Character:
	def __init__(self, name, **kwargs):
		self.name = name

		for key, value in kwargs.items():
			setattr(self, key, value)