import requests
from datetime import datetime

USERNAME = "python-dev"
TOKEN = "pythonsecret"


PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "graph3",
    "name": "Python Graph",
    "unit": "meters",
    "type": "float",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"

# today_date = datetime(year=2025, month=7, day=30).strftime("%Y%m%d")
today_date = datetime.now().strftime("%Y%m%d")

pixel_config = {
    "date": today_date,
    "quantity": "87",
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)


update_pixel_endpoint = f"{pixel_endpoint}/{pixel_config['date']}"

new_data = {
    "quantity": input("How much percentage you work on python program today?: e.g 87, 45: "),
}

response = requests.put(url=update_pixel_endpoint, json=new_data, headers=headers)
print(response.text)


delete_pixel_endpoint = f"{pixel_endpoint}/{pixel_config['date']}"
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)



# Possible errors by HTTP response status code
# 400 Bad Request
# This is an error if there is some mistake in your request. Unless the mistake is corrected, the request will not succeed.
# 403 Forbidden
# This error occurs when Pixela is unable to process your request due to its terms or specifications.
# 404 Not Found
# This error occurs when your request destination does not exist.
# This error also occurs when authentication to the request destination is not successful.
# 409 Conflict
# This error occurs when your request conflicts with something else. Check the message in the response body, and review or retry the request.
# 500 Internal Server Error
# Status in the event of an unexpected error. Retrying the request may be successfully processed.
