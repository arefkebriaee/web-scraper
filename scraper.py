import requests
from bs4 import BeautifulSoup


# ---------------------------------------------------------------
# use BeautifulSoup to access easily to specific part of web page.
# in this example we can access first h1 tag of web page by find method.
# also we can access to all h1 tags by findAll or find_all methods

url = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'

my_request = requests.get(url)
content = BeautifulSoup(my_request.text, 'html.parser')
print(content.find('h1'))
print(content.find_all('h1'))
print(content.findAll('h1'))
