import requests
import json

api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
api_key = "YOUR-API-KEY"
header_dic = {"Authorization": "Bearer " + api_key}
params = {"url": "https://www.linkedin.com/in/vasav-anandjiwala/"}
response = requests.get(api_endpoint, params=params, headers=header_dic)

json_data = response.json()
print("**********")
print(response._content)
file_path = "response_data.json"
with open(file_path, "w") as json_file:
    json.dump(json_data, json_file)

with open("response_data1.json", "wb") as json_file:
    json_file.write(response._content)
