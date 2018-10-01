class ReversedStr(str):
	#__new__ is a class method that doesn't take self
	def __new__(*args, **kwargs):
		self = str.__new__(*args, **kwargs)
		#[::-1] means reversed
		self = self[::-1]
		return self
