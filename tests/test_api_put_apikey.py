import requests

url = "https://reqres.in/api/users/2"

headers = {
    "content-type": "application/json",
    "x-api-key": "a5403e70-4573-41a8-af16-c243e58c3d11"
}

payload = {"name": "morpheus", "job": "zion resident"}


response = requests.put(url, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())