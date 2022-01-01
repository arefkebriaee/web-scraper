import requests

# ---------------------------------------------------------------
# send parameters to url.
# we can send parameters inside request by 'params' argument.
# for example we send multiple parameters to server and server return response.
# params must be dictionery.

url = 'http://www.webscrapingfordatascience.com/calchttp/'

parameters = {
    'a': 7,
    'b': 3,
    'op': '+'
}

my_request = requests.get(url, params=parameters)

print(my_request.text)
