import random
from wordle_classes import Answer, Question, Connections, define_connection

def choose_word():
	with open("words.txt", "r") as file:
		text = file.read()
		words = list(map(str, text.split()))
		answer = random.choice(words)
		answer = Answer(answer)
	return answer, words

def check_guessed_word(question, answer):
	output = ""
	connection = define_connection(question.name, answer.name)
	if question.name == answer.name:
		output = "Congrats! You guessed the word \""
		output += answer.name
		output += "\"!"

	elif len(connection.green) > 0:
		guessed = ""
		for i in range(5):
			if i + 1 in connection.green:
				guessed += connection.green[i + 1]
			else:
				guessed += "_"
		output = guessed
	
	if len(output) > 0:
			output += "\n"
	
	if len(connection.yellow) > 0:

		output += "Letters not in place: " if len(connection.yellow) > 1 else "Letter not in place: "
		for letter in connection.yellow:
			output += letter
			output += ", "
		output = output.strip(", ")

	if len(output) == 0:
		output += "No luck this time."
	return output 


answer, words = choose_word()
print("Guess the 5-letter word: \n")

trials = 0

while True:
	while True:
		guessed_word = input()
		if len(guessed_word) != 5:
			print("Word needs to have 5 letters!")
		elif guessed_word not in words:
			print("It must be a real word!")
		else:
			break

	guessed_word = Question(guessed_word)

	output = check_guessed_word(guessed_word, answer)

	print(output)

	if guessed_word.name == answer.name:
		break
	elif trials < 4:
		x = 5 - trials
		print("You have %x more chances!\n" %x)
	elif trials == 4:
		print("You have the last one chance!\n")

	else:
		print("\nYou lost :( \nThe answer is %a." %answer.name)
		break
	trials += 1

# checking
