import requests

# ---------------------------------------------------------------
# send parameters to url.
# we can send parameters inside request by 'params' argument.
# for example we send 'car' as query to server.
# params must be dictionery.

url = 'http://www.webscrapingfordatascience.com/paramhttp/'

parameters = {
    'query': 'car'
}

my_request = requests.get(url, params=parameters)

print(my_request.text)
