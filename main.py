from notion.get_token import get_token
from notion.list_databases import list_databases
from notion.get_documents import get_documents_from_database
import os, requests, json

if __name__ == "__main__":
    token = get_token()

    databases = list_databases(token)
    # print(json.dumps(databases, indent=4))

    for database in databases:
        documents = get_documents_from_database(token, database["id"])
