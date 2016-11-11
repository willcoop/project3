# Use http://collemc.people.si.umich.edu/data/bshw3StarterFile.html as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import requests
import re
from bs4 import BeautifulSoup

fopen = open('index.html', 'w')
base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'lxml')

for each in soup.find_all(text=re.compile('student')):
	change = each.replace('student','AMAZING student')
	each.replace_with(change)

for img in soup.find_all('img'):
	if img['src'] == 'logo2.png':
		img['src'] = 'media/logo.png'

	else:
		img['src'] = 'media/champs.jpg'

new = soup.prettify()

fopen.write(new)

