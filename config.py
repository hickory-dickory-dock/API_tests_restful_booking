import requests
import json
import endpoints

def get_token() -> str:
    headers = {"Content-Type": "application/json; charset=utf-8"}
    with open("Data/auth.json", "r") as f:
        body = json.loads(f.read())
    raw_response = requests.post(url=endpoints.auth, headers=headers, json=body)
    if raw_response.status_code == requests.codes.ok:
        response = json.load(raw_response.text)
        return response["token"]
    else:
        raise ValueError("Status code was not expected: " + str(raw_response.status_code))