import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/" 
username = input("What is your username?\n")
password = getpass("What is your password?\n")

#username and password are passed to get the token from the post request below.
auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password}) 
print(auth_response.json())

if auth_response.status_code == 200:
    #token is stored which has been returned by the post method above.
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/products/" 
     
    #token is provided in the authorization header.
    get_response = requests.get(endpoint, headers=headers) 
    print(get_response.json())