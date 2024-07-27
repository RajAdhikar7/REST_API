import requests

endpoint = "http://localhost:8000/api/products/1/update/" 

data = {
    "title": "This Is Water park",
    "price": 34.00
}

get_response = requests.put(endpoint, json=data) 
print(get_response.json())