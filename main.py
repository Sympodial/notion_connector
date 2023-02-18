from notion import list_databases
import os, requests, json

from dotenv import load_dotenv
load_dotenv()

token = os.environ.get("NOTION_TOKEN")

if __name__ == "__main__":
    databases = list_databases(token)
    # print(json.dumps(databases, indent=4))

    for database in databases:
        print(database["id"])
