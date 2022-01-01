import requests


url = 'http://www.webscrapingfordatascience.com/'

my_request = requests.get(url)

print(my_request.text)
