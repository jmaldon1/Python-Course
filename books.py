class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author

	def __str__(self):
		return '{} by {}'.format(self.title, self.author)

class Bookcase:
	def __init__(self, books = None):
		self.books = books

	#classsmethod's Don't take self as their first argument
	#But instead take the class that they are being called on
	@classmethod
	def create_bookcase(cls, book_list):
		books = []
		for title, author in book_list:
			books.append(Book(title, author))
		return cls(books)