import requests


def create_user(url):
    url = url + "/users/v1/register"
    payload = {
        "username": "name1",
        "password": "pass1",
        "email": "user@tempmail.com",
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print(response.json())  # Handle successful response
    else:
        print(f"Error: {response.status_code}", response.text)  # Handle errors

    return response


if __name__ == "__main__":
    print(create_user("http://127.0.0.1:5000"))
