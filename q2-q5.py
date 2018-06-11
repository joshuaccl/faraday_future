# File: q2-q5.py
# Author: Joshua Lam
# Info: File containing the answers to questions 2 through 5

# Question 2

# Takes in a string and returns int, float, or string depending
# on whether the string can be converted to a float or integer
def convert(string):
	try:
		integer = int(string)
		return integer
	except ValueError:
		try:
			f = float(string)
			return f
		except ValueError:
			return string

# Test for question two
def test_two():
	print("Question two test")
	test = str(input("Enter a string to convert ('q' to quit): "))
	while test != 'q':
		print(convert(test), type(convert(test)))
		test = str(input("Enter a string to convert ('q' to quit): "))


# Driver for testing question 2 and 5
action = input("'q' to quit, '2' or '5' to test corresponding question: ")
while action != 'q':
	if action == '2':
		test_two()
	elif action == '5':
		test_five()
	else:
		print("Please enter 'q', '2', or '5' only")
	action = input("'q' to quit, '2' or '5' to test corresponding question: ")


