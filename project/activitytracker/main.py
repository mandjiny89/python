import requests
import datetime

pixe_api_url = "https://pixe.la/v1"
user_name = "username"
user_password = "password"

# user_parameters = {
#               "token": user_password,
#               "username": user_name,
#               "agreeTermsOfService": "yes",
#               "notMinor": "yes"
# }

graph_parameters = {
            "id": "codinggraph",
            "name": "codinggraph",
            "unit": "hours",
            "type": "int",
            "color": "momiji",
}

headers = {
          "X-USER-TOKEN": user_password
}

# Post graph
# response = requests.post(f"{pixe_api_url}/users/{user_name}/graphs",  json=graph_parameters, headers=headers)
#put request
# https://pixe.la/v1/users/a-know/graphs/test-graph
# response = requests.put(f"{pixe_api_url}/users/{user_name}/graphs/codinggraph",  json=graph_parameters, headers=headers)

#Delete request
# response = requests.delete(f"{pixe_api_url}/users/{user_name}/graphs/codinggraph", headers=headers)

today = datetime.now()
# today = datetime(year=2024, month=01, date=20)
graph_pixle = {
            "date": today.strftime("%Y%m%d"),
            "quantity": "4",
}

# Post pixle
# /v1/users/<username>/graphs/<graphID>
# response = requests.post(f"{pixe_api_url}/users/{user_name}/graphs/codinggraph",  json=graph_pixle, headers=headers)

# update pixle
# /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>


print(response.text)