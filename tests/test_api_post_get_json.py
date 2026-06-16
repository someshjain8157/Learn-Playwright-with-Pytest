import json
import pytest


def load_test_data():
    with open("testdata/users.json", "r") as f:
        return json.load(f)


TEST_DATA = load_test_data()


@pytest.mark.parametrize("user_data", TEST_DATA)
def test_create_user(playwright, user_data):

    request_context = playwright.request.new_context()

    response = request_context.post(
        "https://reqres.in/api/users",
        data=user_data,
        headers={
            "x-api-key": "reqres_7db3d4a09a9a4c588a77dae9f4d4029b"
        }
    )

    assert response.status == 201

    response_json = response.json()

    print("\nCreated User:")
    print(response_json)

    request_context.dispose()


def test_get_users(playwright):

    request_context = playwright.request.new_context()

    response = request_context.get(
        "https://reqres.in/api/users?page=2",
        headers={
            "x-api-key": "reqres_7db3d4a09a9a4c588a77dae9f4d4029b"
        }
    )

    assert response.status == 200

    users = response.json()

    print("\nUsers from API:")
    print(json.dumps(users, indent=4))

    request_context.dispose()