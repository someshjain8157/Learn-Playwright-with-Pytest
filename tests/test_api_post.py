import requests


def test_api_post_creates_resource():
	url = "https://jsonplaceholder.typicode.com/posts"
	headers = {"Content-Type": "application/json"}
	data = {"title": "Playwright", "body": "API Testing", "userId": 1}

	response = requests.post(url, headers=headers, json=data)

	# verify correct status and response body
	assert response.status_code == 201
	body = response.json()
	assert body.get("title") == "Playwright"
	assert body.get("body") == "API Testing"
	assert body.get("userId") == 1