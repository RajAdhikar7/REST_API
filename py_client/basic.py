import requests

# endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query": "Hello world"}) # HTTP Request
print("this is text",get_response.text) # print raw text response


# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Nototion ~ Python Dict
print("this is json",get_response.json())
print("this is status code",get_response.status_code)