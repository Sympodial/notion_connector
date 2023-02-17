import os
import requests, json
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get("NOTION_TOKEN")
database_id = os.environ.get("NOTION_DATABASE_ID")

def readDatabase(database_id, token):

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
    print(res.status_code)
    output_json = res.json()
    print(json.dumps(output_json, indent=4))

    """
    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
    """


if __name__ == "__main__":
    readDatabase(database_id, token)
