# File: q1.py
# Author: Joshua Lam
# Info: Contains the UFList class which stores items and can return
# 	the unique elements and also the frequency of elements.

# Unique and Frequency List
class UFList:

	# Initialize a class instance
	def __init__(self, items=None):
		if items:
			self.items = items
		else:
			self.items = []
		self.init_frequency(items)
		self.init_unique()
	
	# Function to initialize the unique items of a list
	def init_unique(self):
		self.unique = set()
		if not self.frequency:
			return
		for item in self.frequency:
			if self.frequency[item]==1:
				self.unique.add(item)
	
	# Function to initialize frequency of items in a list
	def init_frequency(self, items):
		self.frequency = {}
		if not items:
			 return
		for item in items:
			if item in self.frequency:
				self.frequency[item] += 1
			else:
				self.frequency[item] = 1
	
	# Insert item into list and update unique and frequency
	def insert(self, position, item):
		self.items.insert(position, item)
		self.update_unique(item)
		self.update_frequency(item)

	# Append item to end of list and update unique and frequency
	def append(self, item):
		self.items.append(item)
		self.update_unique(item)
		self.update_frequency(item)

	# Function to update the unique items
	def update_unique(self, item):
		if item in self.unique:
			self.unique.remove(item)
		elif item not in self.frequency:
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
