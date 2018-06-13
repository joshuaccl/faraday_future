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

# Question 3

# Reformatted code
args = {'animal':'dog', 'name':'Fido', 'age':10}
output = ('{0[name]} the {0[animal]} is {0[age]} years old'.format(args))

# Debug line
# print(output)

# Question 4

# Function that returns the minimum of x, y, and z
def three_min(x, y, z):
	temp = custom_min(x, y)
	return custom_min(temp, z)	

# Helper function which returns the minimum of x and y
def custom_min(x, y):
	if x < y:
		return x
	else:
		return y
	

# Test for question two
def test_two():
	print("Question two test")
	test = str(input("Enter a string to convert ('q' to quit): "))
	while test != 'q':
		print(convert(test), type(convert(test)))
		test = str(input("Enter a string to convert ('q' to quit): "))

# Test for question four
def test_four():
	print("Question four test")
	while 1:
		one = input("Enter the first number ('q' to quit): ")
		if one == 'q':
			break
		two = input("Enter the second number ('q' to quit): ")
		if two == 'q':
			break
		three = input("Enter the third number ('q' to quit): ")
		if three == 'q':
			break
		print("The minimum is " + three_min(one, two, three))

# Driver for testing question 2 and 4
action = input("'q' to quit, '2' or '4' to test corresponding question: ")
while action != 'q':
	if action == '2':
		test_two()
	elif action == '4':
		test_four()
	else:
		print("Please enter 'q', '2', or '4' only")
	action = input("'q' to quit, '2' or '4' to test corresponding question: ")


