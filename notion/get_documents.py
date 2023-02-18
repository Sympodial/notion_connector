import requests
from notion.exceptions import APIException

def get_documents_from_database(token, database_id):
    print(f"Token: {token}")
    print(f"Database: {database_id}")

    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    payload = {}

    url = f'https://api.notion.com/v1/'

    res = requests.request("POST", url, headers=headers, json=payload)
    data = res.json()

    if res.status_code == 200:
        return data["results"]
    else:
        raise APIException("Invalid credentials or API error")
