import requests


response = requests.get('https://api.github.com')

'''
The response of a GET request often has some valuable information, known as a payload, in the message body. 
Using the attributes and methods of Response, you can view the payload in a variety of different formats.
'''

print(response.json(), end="\n")


'''
The response headers can give you useful information, such as the content type of the response payload and a time limit on how long to cache the response. 
To view these headers, access .headers.
'''

print(response.headers, end="\n")

print(response.headers["Content-Length"], end="\n")

'''
One common way to customize a GET request is to pass values through query string parameters in the URL. To do this using get(), you pass data to params. 
For example, you can use GitHub’s Search API to look for the requests library:.
'''

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:c'},
)

json_response = response.json()
repository = json_response['items'][1]
print(f'Repository name: {repository["name"]}') 
print(f'Repository description: {repository["description"]}')

