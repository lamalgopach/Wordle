class Question:
	def __init__(self, name):
		self.name = name


class Answer:
	def __init__(self, name):
		self.name = name

class Connections:
	def __init__(self):
		self.green = {}
		self.yellow = set()


def define_connection(question, answer):
	connection = Connections()
	for i, letter in enumerate(answer):
		if letter == question[i]:
			connection.green[i + 1] = letter
			connection.green[letter] = i + 1
		elif letter in question:
			connection.yellow.add(letter)
	for letter in connection.green:
		if letter in connection.yellow:
			connection.yellow.remove(letter)
	return connection