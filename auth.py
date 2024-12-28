
import requests
import base64
from urllib.parse import unquote

# Your client_id, client_secret, and redirect_uri
client_id = 'a35a0e___(_____)___d4bb92b'
client_secret = '6b889b___(_____)___2b91'
redirect_uri = 'https://ghhggjkgdfhjkhkgjgj.nl/callback'

# Your authorization code (from the URL, make sure it's decoded)
authorization_code = unquote('AQAieGYTX9xAsVSmf7U0aIRrpuVzfI67IOG6WvispKhvH45p1fiJFxOOncLqlQs2SeJ0SIobWfYUPa1hv1f5p3NKDXLw7ebTNEkIxLYOCsvJ23rUl1bdTuZGAaIBoTh-s0WiC8QPmSA1t7__g1Tw___(_____)___JbYRjHgJAGEnQ5_SDLLwKypPuNw')

# Create the token request
token_url = "https://accounts.spotify.com/api/token"
headers = {
    'Authorization': 'Basic ' + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode(),
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = {
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'redirect_uri': redirect_uri
}

# Make the request
response = requests.post(token_url, headers=headers, data=data)

# Parse the response
try:
    token_info = response.json()
    print(token_info)
except ValueError:
    print("Failed to parse JSON response.")
    print(response.text)

# Extract access_token if it's present
if 'access_token' in token_info:
    access_token = token_info['access_token']
    print(f"Access Token: {access_token}")
else:
    print("No access token found in the response.")
