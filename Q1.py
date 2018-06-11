# File: one.py
# Author: Joshua Lam

# Unique and Frequency List
class UFList:

	# Initialize a class instance
	def __init__(self):
		self.items = []
		self.unique = set()
		self.frequency = {}

	# Initialize a class instance with a list
	def __init__(self, items):
		self.items = items
		self.unique = set(items)
		self.frequency = init_frequency(items)
	
	# Insert item into list and update unique and frequency
	def insert(self, position, item):
		self.items.insert(position, item)
		update_unique(item)
		update_frequency(item)

	# Append item to end of list and update unique and frequency
	def insert(self, item):
		self.items.append(item)
		update_unique(item)
		update_frequency(item)

	# Function to initialize frequency of items in a list
	def init_frequency(items):
		frequency = {}
		for item in items:
			if item in frequency:
				frequency[item] += 1
			else:
				frequency[item] = 1

	# Function to update the unique items
	def update_unique(self, item):
		if item in self.unique:
			self.unique.remove(item)
		else:
			self.unique.add(item)

	# Function to update the frequency of items
	def update_frequency(self, item):
		if item in self.frequency:
			self.frequency[item] += 1
		else:
			self.frequency[item] = 1

	# Returns the unique items
	def get_unique(self):
		return self.unique

	# Returns the frequency of items
	def get_frequency(self):
		return self.frequency
