import requests

url = "https://api.restful-api.dev/collections"

# Example API key (replace with your actual key)
api_key = "a5403e70-4572-41c8-bf16-c243e58c3d81"

headers = {
    "x-api-key": api_key,   # Some APIs use "Authorization": f"Bearer {api_key}"
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())