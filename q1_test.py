# File: q1_test.py
# Author: Joshua Lam
# Info: File contains the test driver for the UFList class

from q1 import UFList

# Tests a list from scratch.
def q1_test_one():
	print("Conducting test case one...")
	list_one = UFList()
	
	# Populate the list.
	for i in range(0,5):
		list_one.append(i)
	
	print("The list currently is...")
	print(list_one.items)

	print("Inserting items")

	list_one.insert(3,3)
	list_one.insert(2,3)
	list_one.insert(6,4)
	list_one.insert(1,0)
	
	print("The list currently is...")
	print(list_one.items)

	print("The unique items in the list are:")
	print(list_one.get_unique())

	print("The frequency of the items are:")
	print(list_one.get_frequency())

# Tests a list from initial list of items.
def q1_test_two():
	print("Conducting test case two...")
	items = [0,1,2,3,4,3,3,4,0]
	list_two = UFList(items)
	
	print("The list currently is...")
	print(list_two.items)
	
	print("The unique items in the list are:")
	print(list_two.get_unique())

	print("The frequency of the items are:")
	print(list_two.get_frequency())

q1_test_one()
q1_test_two()
