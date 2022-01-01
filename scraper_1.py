import requests
from bs4 import BeautifulSoup


# ---------------------------------------------------------------
# we can access to an element of web page and also access to attributes of element
# likes name, content, text,... and access to id, class,... by get method.
# if element has not attribute return None.

url = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'

my_request = requests.get(url)
content = BeautifulSoup(my_request.text, 'html.parser')
element = content.find('h1')

print(element)
print(element.name)
print(element.contents)
print(element.text)
print(element.get('class'))
print(element.get('id'))
print(element.get('lang'))
