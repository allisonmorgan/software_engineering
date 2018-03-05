from bs4 import BeautifulSoup
import requests
import re

pet_types = ['dogs', 'cats', 'small_animals']
pet_pages = ['https://www.boulderhumane.org/animals/adoption/dogs', 'https://www.boulderhumane.org/animals/adoption/cats', 'https://www.boulderhumane.org/animals/adoption/adopt_other']

pet_delimiter = re.compile('.*views-row views-row-.*')
name_delimiter = 'views-field views-field-field-pp-animalname'
primary_breed_delimiter = 'views-field views-field-field-pp-primarybreed'
secondary_breed_delimiter = 'views-field views-field-field-pp-secondarybreed'
age_delimiter = 'views-field views-field-field-pp-age'

zoo = {}

for i, pet_page in enumerate(pet_pages):
	try:
		r = requests.get(pet_page)
	except:
		continue

	html = r.text
	soup = BeautifulSoup(html, 'html.parser')


	# Find all of the pets listed on that page
	pets = []
	for pet in soup.find_all('div', {'class': pet_delimiter}):

		# Find the name, breeds, and age of this pet
		name = pet.find('div', {'class': name_delimiter}).get_text(strip=True)
		primary_breed = pet.find('div', {'class': primary_breed_delimiter}).get_text(strip=True)
		secondary_breed = pet.find('div', {'class': secondary_breed_delimiter}).get_text(strip=True)
		age = pet.find('div', {'class': age_delimiter}).get_text(strip=True)
		age = re.sub(r'^Age:', '', age) # Age information is prefixed with "Age:" in the text

		# Add this pet to our list
		pets.append({'name': name, 'breeds': [primary_breed, secondary_breed], 'age': age})

	# Add all of the pets of this type to our list
	zoo[pet_types[i]] = pets

for pet_type in pet_types:
	print pet_type
	for each in zoo[pet_type]:
		print each


