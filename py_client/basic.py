import requests


endpoint = "http://localhost:8000/api/" #http://127.0.0.1:8000/

get_response = requests.post(endpoint, json={"title": "Abc123", "content": "Hello world", "price": "134.30"}) # HTTP Request
# HTTP Request -> HTML
# REST API HTTP Request -> JSON

print(get_response.json())
# print("this is status code",get_response.status_code) 

