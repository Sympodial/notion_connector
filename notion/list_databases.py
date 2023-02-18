import os
import requests, json

def list_databases(token):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    payload = {
        "filter": {
            "value": "database",
            "property": "object",
        },
    }

    url = f"https://api.notion.com/v1/search"

    res = requests.request("POST", url, headers=headers, json=payload)
    data = res.json()
    output = res.json()

    if res.status_code == 200:
        return output["results"]

    """
    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
    """
