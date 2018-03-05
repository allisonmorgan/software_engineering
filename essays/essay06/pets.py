from bs4 import BeautifulSoup
import requests

pets = ['dogs', 'cats', 'small_animal']
petpages = ['https://www.boulderhumane.org/animals/adoption/dogs', 'https://www.boulderhumane.org/animals/adoption/cats', 'https://www.boulderhumane.org/animals/adoption/adopt_other']
zoo = {}

for i, petpage in enumerate(petpages):
	try:
		r = requests.get(petpage)
	except:
		continue

	html = r.text
	soup = BeautifulSoup(html, 'html.parser')

	# What's the title of this page?
	print soup.title.string




