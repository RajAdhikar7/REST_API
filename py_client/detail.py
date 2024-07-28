import requests

headers = {'Authorization': 'Bearer 447ecf7c7440335d8d28f650b3ccdfab70f45094'}
endpoint = "http://localhost:8000/api/products/1/" 

get_response = requests.get(endpoint,headers=headers) 
print(get_response.json())



