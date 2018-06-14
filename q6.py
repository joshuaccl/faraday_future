# File: q6.py
# Author: Joshua Lam
# Info: File implementing a simple California City GUI

from appJar import gui
import json

# Various methods
def create_new_field(name, text):
	app.addLabelEntry(name)
	app.setLabel(name, text)

def set_entry_contents(entry, contents):
	app.setEntry(entry, contents)

def get_data(city, data):
	return cities_dictionary[city][data]

def update_entry(data):
	info = get_data(app.getOptionBox('City'), data)
	set_entry_contents(data, info)	

# Updates all the fields
def update_entry_contents():
	update_entry('full_county_name')
	update_entry('primary_latitude')
	update_entry('primary_longitude')

# Read in data
filename = input('Please enter the json city file name: ')
with open(filename) as json_file:
	cities = json.load(json_file) # cities is a list

# Transfer cities into a dictionary and list
cities_dictionary = {}
cities_list = []
for city in cities:
	cities_dictionary[city['name']] = city
	cities_list.append(city['name'])
cities_list.append('')
cities_list.sort()

# Intialize the GUI
app = gui()
app.addLabel('title', 'City Information')

# Get the cities to display in the drop down list
app.addLabelOptionBox('City', cities_list)

# Create the data fields
create_new_field('full_county_name', 'County')
create_new_field('primary_latitude', 'Latitude')
create_new_field('primary_longitude', 'Longitude')

app.setOptionBoxChangeFunction('City', update_entry_contents)

app.go()
